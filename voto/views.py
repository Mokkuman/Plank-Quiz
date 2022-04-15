from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from usuario.models import User,Flashcard,Practica
from voto.models import VotoFlash,VotoPract

# Create your views here.
def votoDoc(request):
    if request.POST.get('action')=='post':
        doc_id = int(request.POST.get('id'))
        doc = get_object_or_404(Flashcard,id=doc_id)
        user = request.user
        VotoFlash.give_vote(user,doc,int(request.POST.get('tipo')))
        response = {'voto':VotoFlash.get_voto(doc)}
        return JsonResponse(response)
    
def votoPract(request):
    if request.POST.get('action')=='post':
        pract_id = int(request.POST.get('id'))
        pract = get_object_or_404(Practica,id=pract_id)
        user = request.user
        VotoPract.give_vote(user,pract,int(request.POST.get('tipo')))
        response = {'voto':VotoPract.get_voto(pract)}
        return JsonResponse(response)