from django.shortcuts import render
from django.http import HttpResponse #prueba, first commit

# Create your views here.
def home(request):
    return HttpResponse("Hola esto plank OwO")