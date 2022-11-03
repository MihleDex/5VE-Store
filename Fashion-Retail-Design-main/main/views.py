from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from .forms import  RegisterForm, CustomAuthForm, NewsFieldForm
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.views import LoginView
from django.views.generic import ListView,DetailView
from django.contrib import messages
from django.http  import JsonResponse
from .models import Items
import json

class CustomLoginView(LoginView):
    authentication_form =  CustomAuthForm
# Create your views here.
def index(request):
    items = Items.objects.all()
    form = NewsFieldForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect("/home")

    return render(request,"index.html",{'form':form,'items':items})

def signup(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request,user)
            return redirect('/home')
    else:
        form = RegisterForm()
    return render(request,'registration/signup.html',{"form":form})

def login(response):
    if response.method == 'POST':
        form = CustomAuthForm(response.POST)
        if form.is_valid():
            user = form.save()
            login(response.user)
            messages.success(response,f'{user.first_name} has logged in!')
            return redirect('/home')
    else:
        form = CustomAuthForm()
    return render(response,'registration/login.html',{'form':form})

def product(request):
    return render(request,'product.html')

