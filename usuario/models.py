from django.db import models
from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin

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

class Tema(models.Model):
  descripcionTema = models.CharField(max_length=100, blank = False)    
class Flashcard(models.Model):
    user = models.ForeignKey(User, null = True, on_delete=models.SET_NULL)
    tema = models.ForeignKey(Tema, null = True, on_delete = models.SET_NULL)
    titulo = models.CharField(max_length=100, blank=False)
    contenido = models.CharField(max_length=1000, blank = False)
    visible = models.BooleanField(default = True)
    descripcion = models.CharField(max_length=100, blank = False)
    
class Practica(models.Model):
    user = models.ForeignKey(User,null = True, on_delete=models.SET_NULL)
    tema = models.ForeignKey(Tema, null = True, on_delete = models.SET_NULL)
    descripcion = models.CharField(max_length=100, blank= False)
