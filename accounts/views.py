from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth

def signup(request):
    print('i am here')
    if request.method =='POST':
        #user has info and wants an account now!
        if request.POST['password1'] ==request.POST['password2']:
            try:
               user=User.objects.get(username=request.POST['username'])
               print('user is:', user)
               return render(request,'accounts/signup.html',{'error':'Username has already been taken '}) 
            except User.DoesNotExist:
                user=User.objects.create_user(request.POST['username'], password=request.POST['password1']) 
                auth.login(request, user) 
                return render(request,'index.html')
        else:
            return render(request,'accounts/signup.html',{'error':'password must match'}) 
    else:
        #user wants to enter info
        return render(request,'accounts/signup.html')

def login(request):
    return render(request,'accounts/login.html')

def logout(request):
    return render(request,  'accounts/login.html')
