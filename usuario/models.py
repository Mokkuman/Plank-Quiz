from django.db import models
from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin
from tinymce import models as tinymce_models

from .managers import UserManager

class User(AbstractBaseUser,PermissionsMixin):
    #ID annadida por django por defecto
    nombre = models.CharField(max_length=100,blank=False)
    apellido = models.CharField(max_length=100, blank=True)
    email = models.EmailField(max_length=255, unique= True)
    password = models.CharField(max_length=200)
    #imagenPerfil = models.ImageField(...)
    
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
    
    class Meta:
        abstract = True

#Comparte los atributos de herramienta, solo se añade el editor de texto
class Flashcard(Herramienta):
    contenido = tinymce_models.HTMLField()  #Para el editor de texto

#Comparte los atributos de Herramienta, también sirve para tener la llave primaria 
#para relacionar las preguntas
class Practica(Herramienta):
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

#Clase solo para tener una primarykey para asociar las respuestas cerradas
class Cerrada(Pregunta):
    pass

#Clase para definir las respuestas cerradas de una pregunta de tipo Cerrada
#Se hace de esta forma para que el usuario pueda definir "n" respuestas
#Cuenta con la llave foránea de la clase Cerrada para identificar a la clase que pertenecen
class RespuestaCerrada(models.Model):
    id_pregunta = models.ForeignKey(Cerrada,null=True,on_delete=models.SET_NULL)
    respuesta = models.CharField(blank=False, max_length=100)