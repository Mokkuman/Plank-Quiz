from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from usuario.models import User,Flashcard,Practica
from voto.models import VotoFlash,VotoPract

# Create your views here.
def votoFlash(request):
    if request.POST.get('action')=='post':
        flash_id = int(request.POST.get('id'))
        flash = get_object_or_404(Flashcard,id=flash_id)
        user = request.user
        VotoFlash.give_vote(user,flash,int(request.POST.get('tipo')))
        response = {'voto':VotoFlash.get_voto(flash)}
        return JsonResponse(response)
    
def votoPract(request):
    if request.POST.get('action')=='post':
        pract_id = int(request.POST.get('id'))
        pract = get_object_or_404(Practica,id=pract_id)
        user = request.user
        VotoPract.give_vote(user,pract,int(request.POST.get('tipo')))
        response = {'voto':VotoPract.get_voto(pract)}
        return JsonResponse(response)