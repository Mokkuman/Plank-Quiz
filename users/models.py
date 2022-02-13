from enum import unique
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin

from .managers import UserManager

class User(AbstractBaseUser, PermissionsMixin):
    #ID added by django by default
    #profilePic = models.ImageField(default="Planky-Lobo.png",null = True, blank = True)
    firstName = models.CharField(max_length=100,blank=False)
    lastName = models.CharField(max_length=100, blank=True)
    email = models.EmailField(max_length=255, unique= True)
    password = models.CharField(max_length=200)
    
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['firstName'] #email & password are requireed by default
    
    objects = UserManager()
    

