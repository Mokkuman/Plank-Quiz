from django.urls import path,include
from . import views
from usuario import views
from core import views

app_name = 'core'

urlpatterns = [
    path("",views.home,name="home"),
    path("menu/",views.menu,name="menu"),
    path("documento/<int:id>/",views.documento,name="documento"),
    path('nuevoDocumento/',views.nuevoDocumento,name='nuevoDocumento'),
    path("documentos/",views.documentos,name="documentos"),
    path("practicas/",views.practicas,name="practicas"),
    path("nuevaPractica/",views.nuevaPractica,name="nuevaPractica"),
    path('tinymce/',include('tinymce.urls')),#Editor de texto
]
