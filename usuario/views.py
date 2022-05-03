from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from numpy import positive
from core.views import flashcards
import usuario

from voto.models import VotoFlash, VotoPract
from .forms import UserForm, LoginForm, modificarPerfilForm
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

def modificarPerfil(request):

    if request.method=="POST":
             theForm = modificarPerfilForm(request.POST,request.FILES,instance=request.user)
             theForm.actual_user = request.user
             if theForm.is_valid():
                theForm.save()
             return redirect('usuario:perfil')
    else:
         #  return redirect('users:perfil')
         data ={'nombre':request.user.nombre,'apellido':request.user.apellido}
         theForm = modificarPerfilForm(None,initial=data)
    return render(request,"users/modificarPerfil.html",{"form":theForm})

def misFlashcards(request):
    user = request.user
    flashcards = Flashcard.objects.filter(user = user)
    return render(request,'users/misFlashcards.html',{'flashcards':flashcards})

def misPracticas(request):
    user = request.user
    practicas = Practica.objects.filter(user=user)
    return render(request,'users/misPracticas.html',{'practicas':practicas})

def misLikes(request):
    user = request.user
    # filtro de todos los votos positivos de practicas
    votosPositivos = VotoPract.objects.filter(usuario = user, positivo = True)
    practicas = [] # arreglo para juntar practicas
    for votoPositivo in votosPositivos:
        # agrega las practicas gustadas al arreglo
        practica = Practica.objects.get(pk = votoPositivo.id_practica.pk) # sin .pk retorna el titulo de la prac... WHY?
        practicas.append(practica)

    # filtro de todos los votos positivos de flashcards
    votosPositivos = VotoFlash.objects.filter(usuario = user, positivo = True)
    flashcards = [] # arreglo para juntar flashcards
    for votoPositivo in votosPositivos:
        # agrega las practicas gustadas al arreglo
        flashcard = Flashcard.objects.get(pk = votoPositivo.id_flashcard.pk)
        flashcards.append(flashcard)
    return render(request,'users/misLikes.html',{'practicas':practicas, 'flashcards':flashcards})