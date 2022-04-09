from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from .forms import UserForm, LoginForm
from django.contrib.auth.decorators import login_required
from usuario.models import Flashcard, Practica

# Create your views here.


def signup(request):
    signinForm = LoginForm()
    if request.method == "POST":
        signupForm = UserForm(request.POST) #get the form filled out 
        if signupForm.is_valid():
            newUser = signupForm.save(commit=False)
            newUser.save()
            login(request,newUser)
            return redirect('core:home')
    else:
        signupForm = UserForm()
    return render(request, "core/home.html", {"signupForm":signupForm, "signinForm":signinForm})


def signin(request):
    signupForm = UserForm()
    signinForm = LoginForm(request.POST or None)
    if signinForm.is_valid():
        email = signinForm.cleaned_data['email']
        password = signinForm.cleaned_data['password']
        user = authenticate(request, email=email,password=password)
        if user is not None:
            if user.is_active:
                login(request,user)
                #return redirect('usuario:userHome')
                return redirect('core:home')
        else: #User doesn't exist
            signinForm = LoginForm()
            return render(request,"core/home.html",{"signinForm":signinForm, "signupForm": signupForm})  
    return render(request,"core/home.html",{"signinForm":signinForm, "signupForm": signupForm })
    
def signout(request):
    logout(request)
    return redirect("core:home")

def perfil(request):
    return render(request, "users/perfil.html")

# @login_required()
# def Home(request):
#     flash = Flashcard.objects.filter(visible=True).order_by('-voto')[:9]   #Ordena por voto los primeros nueve
#     pract = Practica.objects.filter(visible=True).order_by('-voto')[:9]
#     return render(request, "users/userHome.html",{'flashcard':flash,'practica':pract})

@login_required()
def modificarPerfil(request):
    return render(request, "users/modificarPerfil.html")