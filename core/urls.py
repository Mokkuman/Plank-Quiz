from django.urls import path,include
from . import views
from usuario import views
from core import views

app_name = 'core'

urlpatterns = [
    path("",views.home,name="home"),
    path("flashcard/<int:id>/",views.flashcard,name="flashcard"),
    path('nuevaFlashcard/',views.nuevaFlashcard,name='nuevaFlashcard'),
    path("flashcards/",views.flashcards,name="flashcards"),
    path("practicas/",views.practicas,name="practicas"),
    path("practica/<int:id>/", views.practica, name="practica"),
    #path("nuevaPractica/",views.nuevaPractica,name="nuevaPractica"),
    path("nuevaPractica/",views.nuevaPractica.as_view(),name="nuevaPractica"),
    path('tinymce/',include('tinymce.urls')),#Editor de texto
]
