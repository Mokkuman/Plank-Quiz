from django.urls import path,include
from . import views

app_name = 'core'

urlpatterns = [
    path("",views.home,name="home"),
    path("menu/",views.menu,name="menu"),
    path("documentos/",views.documentos,name="documentos"),
    path("practicas/",views.practicas,name="practicas"),
    path('tinymce/',include('tinymce.urls')),#Editor de texto
]
