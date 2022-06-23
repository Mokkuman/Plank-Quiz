from xml.dom.minidom import Document
from django import forms
from django.forms import TextInput, inlineformset_factory
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
        model = RespuestaCerrada
        fields = ['es_correcta','respuesta']

#Formsets
PregAbiertaFormset = inlineformset_factory(
    Practica,
    Abierta,
    form = PregAbiertaForm,
    extra = 1, #por defecto solo aparece una pregunta abierta
    #mas fields extras
)
# PregCerradaFormset = inlineformset_factory(
#     Practica,
#     Cerrada,
#     form = PregCerradaForm,
#     extra = 0, #por defecto es 0, actualizar con un formset empty
# )
# RespuestaCerradaFormset = inlineformset_factory(
#     Cerrada,
#     RespuestaCerrada,
#     form = RespCerradaForm,
#     extra = 0,
# )