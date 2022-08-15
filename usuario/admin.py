#from atexit import register
from django.contrib import admin

from .models import User,Flashcard,Practica,Cerrada,RespuestaCerrada,Abierta
from voto.models import VotoFlash,VotoPract

class AbiertaInline(admin.TabularInline):
    model = Abierta

class CerradaInline(admin.TabularInline):
    model = Cerrada
    show_change_link = True
    
class RespuestaInline(admin.TabularInline):
    model = RespuestaCerrada

class PracticaAdmin(admin.ModelAdmin):
    list_display= ('titulo','user','filtro','descripcion','visible','voto')
    inlines = [
        AbiertaInline,
        CerradaInline
    ]

class CerradaAdmin(admin.ModelAdmin):
    inlines = [
        RespuestaInline
    ]

    
admin.site.register(User)
admin.site.register(Flashcard)
admin.site.register(Practica, PracticaAdmin)
admin.site.register(Cerrada, CerradaAdmin)
admin.site.register(RespuestaCerrada)
admin.site.register(Abierta)
admin.site.register(VotoFlash)
admin.site.register(VotoPract)