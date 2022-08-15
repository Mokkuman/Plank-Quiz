from email.headerregistry import Address
from pickle import TRUE
from xml.dom.minidom import Document
from django import forms
from django.forms import TextInput, inlineformset_factory
from django.forms.models import BaseInlineFormSet
from django.forms.formsets import DELETION_FIELD_NAME
from usuario.models import Flashcard,Practica,Abierta,Cerrada,RespuestaCerrada

class FlashcardForm(forms.ModelForm):
    class Meta:
        model = Flashcard
        fields = ['titulo','filtro','descripcion','contenido']
        widgets = {
            'titulo': TextInput(attrs={'placeholder':'Título'}),
            'descripcion': TextInput(attrs={'placeholder':'Descripción'}),
        }

class PracticaForm(forms.ModelForm):
    class Meta:
        model = Practica
        fields = ['titulo','filtro','descripcion']
        widgets = {
            'titulo': TextInput(attrs={'placeholder':'Título'}),
            'descripcion': TextInput(attrs={'placeholder':'Descripción'}),
        }
    
class PregAbiertaForm(forms.ModelForm):
    class Meta:
        model = Abierta
        fields = ['planteamiento','respuesta']

class PregCerradaForm(forms.ModelForm):
    class Meta:
        model = Cerrada
        fields = ['planteamiento']

class RespCerradaForm(forms.ModelForm):
    class Meta:
        fields = ['respuesta','es_correcta']
        
#nested Formset
class BaseCerradaFormset(BaseInlineFormSet):
    def add_fields(self, form, index):
        super(BaseCerradaFormset,self).add_fields(form,index)
        
        try:
            instance = self.get_queryset()[index]
            pk_value = instance.pk
        except IndexError:
            instance = None
            pk_value = hash(form.prefix)
        
        form.nested = [
            RespCerradaFormset(data=self.data,
                               instance=instance,
                               #prefix="respCe_%s" % pk_value
                               )
        ]
        # form.nested = RespCerradaFormset(
        #     instance=form.instance,
        #     data = form.data if form.is_bound else None,
        #     files = form.files if form.is_bound else None,
        #     prefix='respCe-%s-%s' %(
        #         form.prefix,
        #         RespCerradaFormset.get_default_prefix()),
        #     extra=1)
    
    def is_valid(self):
        result = super(BaseCerradaFormset,self).is_valid()
        
        if self.is_bound:
            for form in self.forms:
                if hasattr(form,'nested'):
                    
                    result = result and form.nested.is_valid()
        
        return result

    def save_new(self, form, commit=True):
        instance = super(BaseCerradaFormset,self).save_new(form, commit = commit)
        
        form.instance = instance
        
        for nested in form.nested:
            nested.instance = instance
            
        for cd in nested.cleaned_data:
            cd[nested.fk.name] = instance
        
        return instance
    
    def should_delete(self,form):
        """Convenience method for determining if the form’s object will
        be deleted; cribbed from BaseModelFormSet.save_existing_objects."""

        if self.can_delete:
            raw_delete_value = form._raw_value(DELETION_FIELD_NAME)
            should_delete = form.fields[DELETION_FIELD_NAME].clean(raw_delete_value)
            return should_delete

        return False
    def save_all(self,commit=True):
        """Save all formsets and along with their nested formsets."""

        # Save without committing (so self.saved_forms is populated)
        # — We need self.saved_forms so we can go back and access
        #    the nested formsets
        objects = self.save(commit=False)

        # Save each instance if commit=True
        if commit:
            for o in objects:
                o.save()

        # save many to many fields if needed
        if not commit:
            self.save_m2m()

        # save the nested formsets
        for form in set(self.initial_forms + self.saved_forms):
            if self.should_delete(form): continue

            for nested in form.nested:
                nested.save(commit=commit)
    
    # def save(self,commit=True):
    #     result = super(BaseCerradaFormset,self).save(commit=commit)
        
    #     for form in self.forms:
    #         if hasattr(form,'nested'):
    #             if not self._should_delete_form(form):
    #                 form.nested.save(commit=commit)
                    
    #     return result
#Formsets
PregAbiertaFormset = inlineformset_factory(
    Practica,
    Abierta,
    form = PregAbiertaForm,
    extra = 0, #por defecto no aparece pregunta alguna xd
)
PregCerradaFormset = inlineformset_factory(
    Practica,
    Cerrada,
    form = PregCerradaForm, 
    formset = BaseCerradaFormset,
    extra = 1
)
RespCerradaFormset = inlineformset_factory(
    Cerrada,
    RespuestaCerrada,
    form = RespCerradaForm,
    extra = 1
)