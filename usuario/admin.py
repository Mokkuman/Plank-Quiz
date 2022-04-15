from atexit import register
from django.contrib import admin

# Register your models here.
from .models import User,Flashcard,Practica,Cerrada,RespuestaCerrada,Abierta
from voto.models import VotoFlash,VotoPract
admin.site.register(User)
admin.site.register(Flashcard)
admin.site.register(Practica)
admin.site.register(Cerrada)
admin.site.register(RespuestaCerrada)
admin.site.register(Abierta)
admin.site.register(VotoFlash)
admin.site.register(VotoPract)