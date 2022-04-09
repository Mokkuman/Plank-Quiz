from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.http import Http404, HttpResponse
from django.views import View
from plank.settings import LOGIN_URL # globally declared variable for the login page

from usuario.models import Flashcard, Practica
from plank.settings import LOGIN_URL
import usuario # globally declared variable for the login page
#prueba, first commit
from usuario.forms import UserForm, LoginForm
from core.forms import DocumentForm, PracticaForm, PregAbiertaForm,PregCerradaForm
from usuario.models import Flashcard,User
# Create your views here.
def home(request):
    if request.user.is_authenticated:
        flash = Flashcard.objects.filter(visible = True).order_by('-voto')[:9]  #Ordena por voto los primeros nueve
        pract = Practica.objects.filter(visible=True).order_by('-voto')[:9]
        return render(request, "users/userHome.html",{'flashcard':flash,'practica':pract})
    else:
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

@login_required
def nuevaPractica(request):
    if request.method == "POST":
        pracForm = PracticaForm(request.POST or None)
        pregAbierta = PregAbiertaForm(request.POST)
        pregCerrada = PregCerradaForm(request.POST)
        if pracForm.is_valid():
            prac = pracForm.save(commit=False)
            prac.user = User.objects.get(id = request.user.id)
            prac.save()
            return redirect('core:practicas',id=prac.id)
        else:
            return render(request, 'core/nuevaPractica.html',{'form': PracticaForm(),'pregA':PregAbiertaForm,'pregC':PregCerradaForm})
    pracForm = PracticaForm()
    pregAbierta = PregAbiertaForm()
    pregCerrada = PregCerradaForm()
    return render(request,'core/nuevaPractica.html',{'form':pracForm,'pregA':pregAbierta,'pregC':pregCerrada})
        
@login_required
def documento(request,id):
    documento = Flashcard.objects.get(id=id)
    return render(request,"core/documento.html",{"documento":documento})
    

@login_required
def nuevoDocumento(request):
    if request.method == "POST":
        form = DocumentForm(request.POST)
        if form.is_valid():
            doc = form.save(commit=False)
            doc.user = User.objects.get(id = request.user.id)
            doc.save()
            return redirect('core:documento',id=doc.id)
        else:
            return render(request,'core/nuevoDocumento.html',{'form':DocumentForm()})
    form = DocumentForm()
    return render(request,'core/nuevoDocumento.html',{'form':form})