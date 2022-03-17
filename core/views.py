from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.views import View
#prueba, first commit
from usuario.forms import UserForm, LoginForm
# Create your views here.
def home(request):
    signupForm = UserForm()
    signinForm = LoginForm()

    return render(request, "core/home.html", {"signupForm":signupForm, "signinForm": signinForm})

@login_required
def menu(request):
    return render(request,"core/menu.html")