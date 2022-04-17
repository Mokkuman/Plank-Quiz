import django_filters

from usuario.models import Flashcard,Practica

class FlashcardFilter(django_filters.FilterSet):
    class Meta:
        model = Flashcard
        fields = ['titulo','filtro']
        
class PracticaFilter(django_filters.FilterSet):
    class Meta:
        model = Practica
        fields = ['titulo','filtro']