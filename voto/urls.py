from django.urls import URLPattern, path
from voto import views

app_name = 'voto'

urlpatterns=[
    path('votoPract/',views.votoPract,name='votoPract'),
    path('votoFlash/',views.votoFlash,name="votoFlash"),
]