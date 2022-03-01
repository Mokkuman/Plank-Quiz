from django import forms
from django.forms import ModelForm, fields
from django.contrib.auth.forms import UserCreationForm
from .models import User

class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('nombre','apellido','email')
        widgets = {
        'nombre': forms.TextInput(attrs = {'class': 'form-control my-3'}),
        'apellido': forms.TextInput(attrs = {'class': 'form-control my-3'}),
        'email': forms.TextInput(attrs = {'class': 'form-control my-3', 'id':'signup_email'}),
        #'password': forms.PasswordInput(attrs = {'class': 'form-control my-3'}),
        #'password2': forms.PasswordInput(attrs = {'class': 'form-control my-3'}),
        }

class LoginForm(forms.Form):
    email = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control my-3', 
    'placeholder':'E-mail',
    'id':'signin_email'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control my-3',
     'placeholder': 'Contraseña'}))

    fields = ['email', 'password']