from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from .forms import UserForm, LoginForm
# Create your views here.


def signup(request):
    #no necesita checar si es POST porque esta función sólo se llama cuando se hace un POST
    theForm = UserForm(request.POST) #get the form filled out 
    if theForm.is_valid():
        newUser = theForm.save(commit=False)
        newUser.save()
        login(request,newUser)
        return redirect('core:home')
    return redirect('core:home')

def signin(request):
    signupForm = UserForm()
    signinForm = LoginForm(request.POST or None)
    if signinForm.is_valid():
        email = signinForm.cleaned_data['email']
        password = signinForm.cleaned_data['password']
        user = authenticate(request, email=email,password=password)
        if user is not None:
            if user.is_active:
                login(request,user)
                return redirect('core:home')
            else: #User doesn't exist
                return render(request,"core/home.html",{"signupForm":signupForm, "signinForm": signinForm,"msg":'No existe el usuario'})
    return redirect('core:home')
    
def signout(request):
    logout(request)
    return redirect("core:home")