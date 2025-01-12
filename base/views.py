from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from .models import CompanyUser
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.
def signup_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        position = request.POST.get('position')
        if CompanyUser.objects.filter(username=username).exists():
            messages.error(request,"User already exists")
            return redirect('login')
        User = CompanyUser.objects.create(username=username, password=password, position=position)
        login(request,User)
        return redirect('home')
    return render(request, 'signup.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        User = authenticate(username = username, password = password)
        if User:
            return redirect('home')
        else: 
            messages.error(request,"User does not exist")
            return redirect('signup')
    return render(request, 'login.html')

def logout_view(request):
    logout(request)
    return redirect('login')

@login_required(login_url='login')
def home(request):
    return render(request, 'home.html')