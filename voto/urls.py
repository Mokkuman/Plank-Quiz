from django.urls import URLPattern, path
from voto import views

app_name = 'voto'

urlpatterns=[
    path('votoPract/',views.votoPract,name='votoPract'),
    path('votoDoc/',views.votoDoc,name="votoDoc"),
    #Poner acá el views que manejará los votos de Practica
]