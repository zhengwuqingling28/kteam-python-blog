from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import RegistrationForm
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm

def index(req):
    return render(req, 'pages/home.html')
def contact(req):
    return render(req, 'pages/contact.html')
def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')  # Điều hướng đến trang chủ
    else:
        form = RegistrationForm()
    return render(request, 'pages/register.html', {'form': form})
def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect('/')  # Điều hướng đến trang chủ
    else:
        form = AuthenticationForm()
    return render(request, 'pages/login.html', {'form': form})
def user_logout(request):
    logout(request)
    return redirect('/') # Điều hướng đến trang chủ
