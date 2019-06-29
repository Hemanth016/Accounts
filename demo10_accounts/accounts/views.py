# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from models import User
from django.contrib import messages
# Create your views here.
def login(request):
    if request.method == 'POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        print('successfully login')
        return redirect('/')
    else:
        return render(request,'login.html')
def register(request):
    if request.method == 'POST':
        name=request.POST['name']
        password=request.POST['password']
        email=request.POST['email']
        phoneno=request.POST['phoneno']
        user=User(name=name,password=password,email=email,phoneno=phoneno)
        user.save()
        print('user created')
        return redirect('/')

    else:
        return render(request,'register.html')

def index(request):
    all_details=User.objects.all()
    return render(request,'index.html',{'user':all_details})
