from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.views import View
from plank.settings import LOGIN_URL # globally declared variable for the login page
#prueba, first commit
from usuario.forms import UserForm, LoginForm
# Create your views here.
def home(request):
    signupForm = UserForm()
    signinForm = LoginForm()

    return render(request, "core/home.html", {"signupForm":signupForm, "signinForm": signinForm})

@login_required()
def menu(request):
    return render(request,"core/menu.html")

def documentos(request):
    return render(request,"core/documentos.html")

def practicas(request):
    return render(request,"core/practicas.html")

def perfil(request):
    return render(request, "core/perfil.html")
