from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin
from django.urls import path, include
from . import views
app_name = 'usuario'
urlpatterns = [
    path('signout', views.signout, name="signout"),
    path('signin', views.signin, name="signin"),
    path('signup', views.signup, name="signup"),
    path('userHome', views.Home, name="userHome"),
    path('modificarPerfil/', views.modificarPerfil, name="modificarPerfil"),
]