from django.contrib.auth import authenticate, forms
from django.core.exceptions import ValidationError
from django.shortcuts import redirect, render
from . import forms

from django.contrib.auth import logout as django_logout,login as auth_login

#python kanalına mesaj gönder
# Create your views here.
def register(request):
    if request.user.is_authenticated:
        return redirect('tasks:home')
    form=forms.RegisterForm()
    if request.method=='POST':
        form=forms.RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('tasks:home')
    context={
        'form':form
    }
    return render(request,'register.html',context)
def logout(request):
    django_logout(request)
    return redirect('customer:login')
def login(request):
    if request.user.is_authenticated:
        return redirect('tasks:home')
    form=forms.LoginForm()
    if request.method=='POST':
        form=forms.LoginForm(request.POST)
        username=request.POST.get('username')
        password=request.POST.get('password')
        account=authenticate(request,username=username,password=password)
        if account is None:
            raise ValidationError(request,'istifadeci adiniz ve ya parolunuz yalnisdir')
        else:
            auth_login(request,account)
            return redirect('tasks:home')
    context={
        'form':form
    }
    return render(request,'login.html',context)