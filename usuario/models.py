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

#class Tema(models.Model):

# class Filtro(models.Model):
#     tema = models.CharField(choices=ELECCION_TEMAS)
#     descripcionTema = models.CharField(max_length=100, blank = False)    

class Flashcard(models.Model):
    user = models.ForeignKey(User, null = True, on_delete=models.SET_NULL)
    #tema = models.ForeignKey(Tema, null = True, on_delete = models.SET_NULL)
    filtro = models.CharField(choices = ELECCION_TEMAS, max_length=50, default=('Matemáticas',('Álgebra','Álgebra')))
    titulo = models.CharField(max_length=100, blank=False)
    contenido = tinymce_models.HTMLField()  #Para el editor de texto
    visible = models.BooleanField(default = True)
    descripcion = models.CharField(max_length=100, blank = False)
    
class Practica(models.Model):
    user = models.ForeignKey(User,null = True, on_delete=models.SET_NULL)
    #tema = models.ForeignKey(Tema, null = True, on_delete = models.SET_NULL)
    filtro = models.CharField(choices = ELECCION_TEMAS, max_length=50, default=('Matemáticas',('Álgebra','Álgebra')))
    descripcion = models.CharField(max_length=100, blank= False)
