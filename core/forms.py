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
        

#Formsets
PregAbiertaFormset = inlineformset_factory(
    Practica,
    Abierta,
    form = PregAbiertaForm,
    extra = 0, #por defecto no aparece pregunta alguna xd
)
# PregCerradaFormset = inlineformset_factory(
#     Practica,
#     Cerrada,
#     form = PregCerradaForm, 
#     formset = BaseCerradaFormset,
#     extra = 1
# )
# RespCerradaFormset = inlineformset_factory(
#     Cerrada,
#     RespuestaCerrada,
#     form = RespCerradaForm,
#     extra = 1
# )