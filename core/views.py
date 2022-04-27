from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.http import Http404, HttpResponse
from django.views import View
#from numpy import gradient
from plank.settings import LOGIN_URL # globally declared variable for the login page
from django.core.paginator import Paginator,EmptyPage
from .filter import FlashcardFilter, PracticaFilter
from django.http import JsonResponse

from usuario.models import Flashcard, Practica
from voto.models import VotoFlash, VotoPract
from plank.settings import LOGIN_URL
import usuario # globally declared variable for the login page
#prueba, first commit
import json
from usuario.forms import UserForm, LoginForm
from core.forms import FlashcardForm, PracticaForm, PregAbiertaForm,PregCerradaForm
from usuario.models import Flashcard,User
from voto.models import VotoFlash,VotoPract
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

@login_required
def flashcards(request):
    context ={}
    filtered_flash = FlashcardFilter(
        request.GET,
        queryset=Flashcard.objects.all().order_by('-voto')
    )
    
    context['filtered_flash'] = filtered_flash
    paginated_filtered_flash = Paginator(filtered_flash.qs,9)   #Cambiar el valor numérico por uno menor para visualizar mejor las paginas
    page_number = request.GET.get('page')
    flash_page_obj = paginated_filtered_flash.get_page(page_number)
    context['flash_page_obj'] = flash_page_obj
    
    return render(request,'core/flashcards.html',context=context)

@login_required
def practicas(request):
    context ={}
    filtered_pract = PracticaFilter(
        request.GET,
        queryset=Practica.objects.all().order_by('-voto')
    )
    
    context['filtered_pract'] = filtered_pract
    paginated_filtered_pract = Paginator(filtered_pract.qs,9)
    page_number = request.GET.get('page')
    pract_page_obj = paginated_filtered_pract.get_page(page_number)
    context['pract_page_obj'] = pract_page_obj
    
    return render(request,'core/practicas.html',context=context)
    
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
def practica(request, id):
    practica = Practica.objects.get(id=id)
    preguntasAbiertas = practica.get_preguntas_abiertas()
    preguntasCerradas = practica.get_preguntas_cerradas()

    if request.method == "POST":
        total = len(preguntasAbiertas) + len(preguntasCerradas)
        answers = request.POST # todo dentro del POST
        #print(answers['answers']) # solo el JSON del POST con nombrePreg:respuesta
        answers = json.loads(answers['answers']) # convierte json en diccionar
        grade = practica.calificar(answers)
        response = {'grade':grade, 'total':total}
        return JsonResponse(response)

    voto = VotoPract.voted(practica,request.user)
    return render(request, "core/practica.html", {
            'practica':practica,
            'abiertas':preguntasAbiertas,
            'cerradas':preguntasCerradas,
            'voto':voto,
            })

@login_required
def flashcard(request,id):
    flashcard = Flashcard.objects.get(id=id)
    voto = VotoFlash.voted(flashcard,request.user)
    return render(request,"core/flashcard.html",{"flash":flashcard,"voto":voto})
    

@login_required
def nuevaFlashcard(request):
    if request.method == "POST":
        form = FlashcardForm(request.POST)
        if form.is_valid():
            doc = form.save(commit=False)
            doc.user = User.objects.get(id = request.user.id)
            doc.save()
            return redirect('core:flashcard',id=doc.id)
        else:
            return render(request,'core/nuevaFlashcard.html',{'form':FlashcardForm()})
    form = FlashcardForm()
    return render(request,'core/nuevaFlashcard.html',{'form':form})