from django.db import models
from usuario.models import User,Flashcard,Practica

# Create your models here.
# Cuando se realice un voto, se creará el objeto Voto para registrarlo correctamente y así evitar que vote multiples veces
class Voto(models.Model):
    #Si ambos son False, entonces es un voto  (No ha votado)
    positivo = models.BooleanField(default=False)
    negativo = models.BooleanField(default=False)
    usuario = models.ForeignKey(User,on_delete=models.SET_NULL,null=True)#Atributo para identificar el usuario que realizó el voto
    
    class Meta:
        abstract = True
        
class VotoPract(Voto):
    id_practica = models.ForeignKey(Practica,null=True,on_delete=models.SET_NULL)
    
    def voted(id_practica,usuario):
        try:    
            voto = VotoPract.objects.get(id_practica=id_practica,usuario = usuario)
        except:
            voto = None
        finally:
            if voto != None:
                if voto.positivo:
                    return 1
                else:
                    return 0
            else:
                return -1
    
    def get_voto(id_practica):
        try:
            voto_final = 0
            votos = VotoPract.objects.filter(id_practica = id_practica) # retorna lista votos de este flashcard
            for voto in votos:
                if voto.positivo:
                    voto_final += 1
                elif voto.negativo:
                    voto_final -= 1
        except:
            pass
        finally:
            id_practica.voto = voto_final
            id_practica.save()
            return voto_final   
        
    
    def give_vote(usuario,id_practica, voto_usuario):
        try:
            voto = VotoPract.objects.get(usuario = usuario, id_practica = id_practica)
            if (voto.positivo and voto_usuario == 1) or (voto.negativo and voto_usuario==-1):
                voto.delete()
            else:
                voto.positivo = not voto.positivo
                voto.negativo = not voto.negativo
                voto.save()
        except:
            if voto_usuario == -1:
                voto = VotoPract.objects.create(usuario = usuario, id_practica = id_practica, negativo = True)
            elif voto_usuario == 1:
                voto = VotoPract.objects.create(usuario = usuario, id_practica = id_practica, positivo = True)
        finally:
            id_practica.voto = VotoPract.get_voto(id_practica)
            id_practica.save()
    
class VotoFlash(Voto):
    id_flashcard = models.ForeignKey(Flashcard,null=True,on_delete=models.SET_NULL)
    
    def voted(id_flashcard,usuario):
        try:    
            voto = VotoFlash.objects.get(id_flashcard=id_flashcard,usuario = usuario)
        except:
            voto = None
        finally:
            if voto != None:
                if voto.positivo:
                    return 1
                else:
                    return 0
            else:
                return -1
    
    def get_voto(id_flashcard):
        voto_final = 0
        try:
            votos = VotoFlash.objects.filter(id_flashcard = id_flashcard) # retorna lista votos de este flashcard
        except:
            return voto_final
        
        for voto in votos:
            if voto.positivo:
                voto_final += 1
            elif voto.negativo:
                voto_final -= 1
        return voto_final
    
    def give_vote(usuario,id_flashcard, voto_usuario):
        try:
            voto = VotoFlash.objects.get(usuario = usuario, id_flashcard = id_flashcard)
            if (voto.positivo and voto_usuario == 1) or (voto.negativo and voto_usuario==-1):
                voto.delete()
            else:
                voto.positivo = not voto.positivo
                voto.negativo = not voto.negativo
                voto.save()
        except:
            if voto_usuario == -1:
                voto = VotoFlash.objects.create(usuario = usuario, id_flashcard = id_flashcard, negativo = True)
            elif voto_usuario == 1:
                voto = VotoFlash.objects.create(usuario = usuario, id_flashcard = id_flashcard, positivo = True)
        finally:
            id_flashcard.voto = VotoFlash.get_voto(id_flashcard)
            id_flashcard.save()