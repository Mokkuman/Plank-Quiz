from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from usuario.models import User,Flashcard,Practica

# Create your views here.
def votoDoc(request):
    if request.POST.get('action')=='post':
        doc_id = int(request.POST.get('id'))
        doc = get_object_or_404(Flashcard,id=doc_id)
        doc.give_vote(User.objects.get(id = request.user.id),int(request.POST.get('tipo')))
        response = {'voto':doc.get_voto()}
        return JsonResponse(response)
    
def votoPract(request):
    pass
    # if request.POST.get('action')=='post':
    #     doc_id = int(request.POST.get('id'))
    #     doc = get_object_or_404(Practica,id=doc_id)
    #     doc.give_vote(User.objects.get(id = request.user.id),int(request.POST.get('tipo')))
    #     response = {'voto':doc.get_voto()}
    #     return JsonResponse(response)