from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.http import Http404, HttpResponse
from django.views import View
from django.views.generic import CreateView
#from numpy import gradient
from plank.settings import LOGIN_URL # globally declared variable for the login page
from django.core.paginator import Paginator,EmptyPage
from .filter import FlashcardFilter, PracticaFilter
from django.http import JsonResponse

from usuario.models import Flashcard, Practica, User
from voto.models import VotoFlash, VotoPract
from plank.settings import LOGIN_URL
import usuario # globally declared variable for the login page
#prueba, first commit
import json
from usuario.forms import UserForm, LoginForm
from core.forms import FlashcardForm, PracticaForm, PregAbiertaFormset
#from usuario.models import Flashcard,User repetido alv
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

class nuevaPractica(CreateView):
    form_class = PracticaForm
    template_name = 'core/nuevaPractica.html'
    
    def get_context_data(self, **kwargs):
        context = super(nuevaPractica,self).get_context_data(**kwargs)
        context['abiertaFormset'] = PregAbiertaFormset(prefix='abiertas')
        print('get_context_data')
        return context
    
    def post(self, request, *args, **kwargs):
        self.object = None
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        abiertaFormset = PregAbiertaFormset(request.POST, prefix='abiertas')
        if(form.is_valid() and abiertaFormset.is_valid()):
            return self.form_valid(form,abiertaFormset)
        else:
            return self.form_invalid(form,abiertaFormset)
        
    def form_valid(self,form,abiertaFormset):
        self.object = form.save(commit = False)
        #Guardando el usuario
        self.object.user = User.objects.get(id = self.request.user.id)
        self.object.save()
        #Guardando abiertaFormset instances
        abiertasSet = abiertaFormset.save(commit=False)
        for ab in abiertasSet:
            ab.practica = self.object
            ab.save()
        return redirect('core:practica',id=self.object.id)
    
    def form_invalid(self,form,abiertaFormset):
        print("Error en los formularios")
        return self.render_to_response(
            self.get_context_data(form = form,
                                  abiertaFormset = abiertaFormset)
        )


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

def flashcard(request,id):
    flashcard = Flashcard.objects.get(id=id)
    voto = VotoFlash.voted(flashcard,request.user)
    return render(request,"core/flashcard.html",{"flash":flashcard,"voto":voto})
    

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