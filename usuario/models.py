from django.db import models
from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin
from tinymce import models as tinymce_models
from .managers import UserManager
from django.urls import reverse

class User(AbstractBaseUser,PermissionsMixin):
    #ID annadida por django por defecto
    nombre = models.CharField(max_length=100,blank=False)
    apellido = models.CharField(max_length=100, blank=True)
    email = models.EmailField(max_length=255, unique= True)
    password = models.CharField(max_length=200)
    imagenPerfil = models.ImageField(upload_to='pfp',default="planky.png",null=True,blank=True)
    
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['nombre'] #email & password estan por default
    
    objects = UserManager()

ELECCION_TEMAS = (
    ('Matemáticas',(
        ('Álgebra','Álgebra'),
        ('Geometría','Geometría'),
        ('Cálculo','Cálculo'),
        )
    ),
    ('Español',(
        ('Lectura y Redacción','Lectura y Redacción'),
        ('Literatura','Literatura'),
        )
    ),
    ('Ciencias Naturales',(
        ('Biología','Biología'),
        ('Química','Química'),
        ('Medicina','Medicina'),
        )
    ),
    ('Humanidades',(
        ('Historia','Historia'),
        ('Filosofía','Filosofía'),
        ('Psicología','Psicología'),
        ),
    )
)

#Para no repetir los atributos comunes entre Flashcard y Práctica
class Herramienta(models.Model):
    user = models.ForeignKey(User,null = True, on_delete=models.SET_NULL)
    filtro = models.CharField(choices = ELECCION_TEMAS, max_length=50, default=('Matemáticas',('Álgebra','Álgebra')))
    titulo = models.CharField(max_length=100, blank=False,default='')
    descripcion = models.CharField(max_length=100, blank= False)
    visible = models.BooleanField(default=True)
    voto = models.IntegerField(default=0)
    
    class Meta:
        abstract = True
    
    def __str__(self):
        return self.titulo

#Comparte los atributos de herramienta, solo se añade el editor de texto
class Flashcard(Herramienta):
    contenido = tinymce_models.HTMLField()  #Para el editor de texto

    def give_vote(self, usuario, voto_usuario):
        try:
            voto = VotoFlash.objects.get(usuario = usuario, id_flashcard = self)
        except:
            voto = None

        if voto is None:
            if voto_usuario == -1:
                voto = VotoFlash.objects.create(usuario = usuario, id_flashcard = self, negativo = True)
            elif voto_usuario == 1:
                voto = VotoFlash.objects.create(usuario = usuario, id_flashcard = self, positivo = True)

    def get_voto(self):
        voto_final = 0
        try:
            votos = VotoFlash.objects.filter(id_flashcard = self) # retorna lista votos de este flashcard
        except:
            return voto_final
        
        for voto in votos:
            if voto.positivo:
                voto_final += 1
            elif voto.negativo:
                voto_final -= 1
        return voto_final
    
    #def get_absolute_url(self):
    #   return reverse("view_flashcard", kwargs={"id" : self.id})
            
    
#Comparte los atributos de Herramienta, también sirve para tener la llave primaria 
#para relacionar las preguntas
class Practica(Herramienta):
    #def get_absolute_url(self):
    #    return reverse("view_practica", kwargs={"id" : self.id})

    def get_preguntas_abiertas(self):
        preguntas_abiertas = Abierta.objects.filter(practica = self)
        return preguntas_abiertas
    
    def get_preguntas_cerradas(self):
        preguntas_cerradas = Cerrada.objects.filter(practica = self)
        return preguntas_cerradas
    
    def calificar(self):
        pass

#Clase abstracta para los diferentes tipos de preguntas
class Pregunta(models.Model):
    practica = models.ForeignKey(Practica,null=True,on_delete=models.SET_NULL)
    planteamiento = models.CharField(blank=False, max_length=100)    
    
    class Meta:
        abstract = True

#Clase para definir las preguntas abiertas
class Abierta(Pregunta):
    respuesta = models.CharField(max_length=100,blank=False)

    def calificar_pregunta(self, respuesta_usuario):
        if respuesta_usuario == self.respuesta:
            return 1
        else:
            return 0


#Clase solo para tener una primarykey para asociar las respuestas cerradas
class Cerrada(Pregunta):
    def get_respuestas(self):
        respuestas = RespuestaCerrada.objects.filter(id_pregunta = self)
        # inside template
        # for PreguntaCerrada in PreguntaCerradas
        #     print(PreguntaCerrada.enunciado)
        #     for RespuestaCerrada PreguntaCerrada.getRespuestasCerradas
        return respuestas

    def calificar_pregunta(self):
        pass
        

#Clase para definir las respuestas cerradas de una pregunta de tipo Cerrada
#Se hace de esta forma para que el usuario pueda definir "n" respuestas
#Cuenta con la llave foránea de la clase Cerrada para identificar a la clase que pertenecen
class RespuestaCerrada(models.Model):
    es_correcta = models.BooleanField(default=False)
    id_pregunta = models.ForeignKey(Cerrada,null=True,on_delete=models.SET_NULL)
    respuesta = models.CharField(blank=False, max_length=100)
    
#Cuando se realice un voto, se creará el objeto Voto para registrarlo correctamente y así evitar que vote multiples veces
class Voto(models.Model):
    #Si ambos son False, entonces es un voto  (No ha votado)
    positivo = models.BooleanField(default=False)
    negativo = models.BooleanField(default=False)
    usuario = models.ForeignKey(User,on_delete=models.SET_NULL,null=True)#Atributo para identificar el usuario que realizó el voto
    
    class Meta:
        abstract = True
        
class VotoPract(Voto):
    id_practica = models.ForeignKey(Practica,null=True,on_delete=models.SET_NULL)
    
class VotoFlash(Voto):
    id_flashcard = models.ForeignKey(Flashcard,null=True,on_delete=models.SET_NULL)