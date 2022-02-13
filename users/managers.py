from lib2to3.pytree import Base
from multiprocessing.sharedctypes import Value
from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import gettext_lazy as _


class UserManager(BaseUserManager):
    def create_superuser(self,email,firstName,password,**other_fields):
        other_fields.setdefault('is_staff',True)
        other_fields.setdefault('is_superuser', True)
        other_fields.setdefault('is_active',True)
        
        if other_fields.get('is_staff') is not True:
            raise ValueError(_('Superuser must have is_staff = True'))
        if other_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser mus have is_superuser = True'))
        
        return self.create_user(email,firstName,password,**other_fields)
    
    def create_user(self,email, firstName, password, **other_fields):
        if not email:
            raise ValueError(_('Debes escribir un email'))
        
        email = self.normalize_email(email)
        user = self.model(email = email, firstName = firstName,
                          password = password, **other_fields)
        user.set_password(password)
        user.save()
        
        return user