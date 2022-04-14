from django.urls import URLPattern, path
from voto import views

app_name = 'voto'

urlpatterns=[
    path('votoDoc/',views.votoDoc,name="votoDoc"),
    #Poner acá el views que manejará los votos de Practica
]