from django.shortcuts import render, redirect

from django.contrib.auth import authenticate,login,logout
from .forms import SignUpForm

from . forms import LoginForm

# Create your views here.
def LoginView(request):
    if request.user.is_authenticated:
        return redirect("post:list")
    form=LoginForm(request.POST or None)
    if form.is_valid():

        username=form.cleaned_data.get('username')
        password=form.cleaned_data.get('password')
        user=authenticate(username=username,password=password)
        login(request,user)
        return redirect('post:list')


    return render(request,'login.html',{'form':form})

def LogoutView(request):
    logout(request)
    return redirect('/')

def SignupView(request):
       form=SignUpForm(request.POST or None)
       if form.is_valid():
            user = form.save(commit=False)
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user.set_password(password)
            user.save()
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('post:list')

       return render(request, 'signup.html',{'form':form})

