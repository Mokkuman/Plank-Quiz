from xml.dom.minidom import Document
from django import forms
from usuario.models import Flashcard,Practica,Abierta,Cerrada

class FlashcardForm(forms.ModelForm):
    class Meta:
        model = Flashcard
        fields = ['titulo','filtro','descripcion','contenido']

class PracticaForm(forms.ModelForm):
    class Meta:
        model = Practica
        fields = ['titulo','filtro','descripcion']
    
class PregAbiertaForm(forms.ModelForm):
    class Meta:
        model = Abierta
        fields = ['planteamiento','respuesta']

class PregCerradaForm(forms.ModelForm):
    class Meta:
        model = Cerrada
        fields = ['planteamiento']