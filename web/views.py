from django import http
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm, User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth import views as auth_views
from . import forms
from django.urls import path


# Create the Web Views - Mudasir ALi

def Index(req):
    return render(req, 'Pages/Index.html')
    


def About(req):
    return render(req, 'Pages/About.html')

def Handle_404(req, exception):
    return render(req, 'Pages/404.html', {'link': f'{req.get_host()}{req.path}'})

# User Authentication

def Signup(req):
    form = forms.CreateUserForm()
    if req.method == 'POST':
        form = forms.CreateUserForm(req.POST)
        if form.is_valid():
            form.save()

            messages.success(req, f'Account was successfully created {form.cleaned_data.get("username")}')
            return redirect('Login')
    
    Content = {'form': form, }
    return render(req, 'Register/Register.html', Content)

def Login(req):
    if req.method == 'POST':
        username = req.POST.get('username')
        password = req.POST.get('password')

        user = authenticate(req, username=username, password=password)

        if user is not None:
            login(req, user)
            return redirect('Index')
        else:
            messages.info(req, 'username or passoword is incorrect')

    return render(req, 'Register/Login.html')

def Logout(req):
    logout(req)
    return redirect('Index')


# Social Media LINKS
def Facebook(req):
    return redirect('https://www.facebook.com/techmub/')

def Github(req):
    return redirect('https://github.com/mudasiralinizamani')

def Twitter(req):
    return redirect('https://twitter.com/Mudasir78169406')

def Website(req):
    return redirect('https://techmudboy.com/')

def Youtube(req):
    return redirect('https://www.youtube.com/channel/UCTc1CZwD4fEGij3yZ9bwRQg?sub_confirmation=1')