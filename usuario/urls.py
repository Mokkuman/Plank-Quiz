from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin
from django.urls import path, include
from . import views
from django.contrib.auth.decorators import login_required

app_name = 'usuario'
urlpatterns = [
    path('signout', views.signout, name="signout"),
    path('signin', views.signin, name="signin"),
    path('signup', views.signup, name="signup"),
    path("perfil/",login_required(views.perfil),name="perfil"),
    path('modificarPerfil/', login_required(views.modificarPerfil), name="modificarPerfil"),
    path('perfil/misFlashcards',login_required(views.misFlashcards),name='misFlashcards'),
    path('perfil/misPracticas',login_required(views.misPracticas),name='misPracticas'),
    path('perfil/misLikes',login_required(views.misLikes),name='misLikes'),
]