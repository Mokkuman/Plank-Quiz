from django.urls import path,include
from . import views
from usuario import views
from core import views
from django.contrib.auth.decorators import login_required


app_name = 'core'

urlpatterns = [
    path("",views.home,name="home"),
    path("flashcard/<int:id>/",login_required(views.flashcard),name="flashcard"),
    path('nuevaFlashcard/',login_required(views.nuevaFlashcard),name='nuevaFlashcard'),
    path("flashcards/",login_required(views.flashcards),name="flashcards"),
    path("practicas/",login_required(views.practicas),name="practicas"),
    path("practica/<int:id>/", login_required(views.practica), name="practica"),
    #path("nuevaPractica/",views.nuevaPractica,name="nuevaPractica"),
    path("nuevaPractica/",login_required(views.nuevaPractica.as_view()),name="nuevaPractica"),
    path('tinymce/',include('tinymce.urls')),#Editor de texto
]
