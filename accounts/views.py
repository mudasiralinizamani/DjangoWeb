from django.shortcuts import render, redirect
from django.http import HttpResponse
from . import forms
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, User




# Create your views here.


def Profile(req):
    return render(req, 'Accounts/Admin.html')

def Signup(req):
    if User.is_authenticated():
        messages.INFO(req, f'You are already Authenticated, {User.username}!')
        return  redirect('Index')
    else:
        form = forms.CreateUserForm()
        if req.method == 'POST':
            form = forms.CreateUserForm(req.POST)
            if form.is_valid():
                form.save()

                messages.success(req, f'Account was successfully created {form.cleaned_data.get("username")}')
                return redirect('Login')
        
        Content = {'form': form, }
        return render(req, 'Accounts/Register.html', Content)

def Login(req):
    if User.is_authenticated():
        messages.INFO(req, f'You are already Logedin, {User.username}!')
        return  redirect('Index')
    else:
        if req.method == 'POST':
            username = req.POST.get('username')
            password = req.POST.get('password')

            user = authenticate(req, username=username, password=password)

            if user is not None:
                login(req, user)
                messages.success(req, f'Successfully login as, {user}')
                return redirect('Index')
            else:
                messages.error(req, 'username or passoword is incorrect')

        return render(req, 'Accounts/Login.html')

def Logout(req):
    logout(req)
    return redirect('Index')

