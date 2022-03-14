from django import forms
from django.forms import ModelForm, fields
from django.contrib.auth.forms import UserCreationForm
from .models import User
from django.contrib.auth import authenticate

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
    
    # def clean_email(self, *args, **kwargs):
    #     email = self.cleaned_data.get("email")
    #     if not email.endswith("buap.mx"):
    #         print("solo buap")
    #         raise forms.ValidationError("Actualmente solo para alumnos buap")
    #     return email

class LoginForm(forms.Form):
    email = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control my-3', 
    'placeholder':'E-mail',
    'id':'signin_email'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control my-3',
     'placeholder': 'Contraseña'}))

    fields = ['email', 'password']

    def clean(self):
        email = self.cleaned_data.get('email')
        password = self.cleaned_data.get('password')
        user = authenticate(email=email, password=password)
        if not user or not user.is_active:
            raise forms.ValidationError("No existe el usuario")
        return self.cleaned_data