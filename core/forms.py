from xml.dom.minidom import Document
from django import forms
from usuario.models import Flashcard

class DocumentForm(forms.ModelForm):
    class Meta:
        model = Flashcard
        fields = ['titulo','filtro','descripcion','contenido']