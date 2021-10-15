from django import forms
from django.http.response import HttpResponse
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ValidationError
from django.forms.forms import Form
from django.shortcuts import get_object_or_404, redirect, render
from . import forms
from .models import List, Task
# Create your views here.
@login_required()
def home(request):
    lists=List.objects.filter(user=request.user)

    form=forms.ListForm()
    if request.method =='POST':
        form=forms.ListForm(request.POST)
        if form.is_valid():
            instance=form.save(commit=False)
            instance.user=request.user
            instance.save()
            return redirect('tasks:home')
        else:
            raise ValidationError('xeta verirem')
    context={'form':form,'lists':lists}

    return render(request,'home.html',context)
def deletelist(request,id):
    list=get_object_or_404(List,id=id)
    if request.user==list.user:
        list.delete()
        return redirect('tasks:home')
    return HttpResponse('ancaq oz commentlerivi sile bilersen.bu commenti sile bilmezsen')
@login_required()
def createtask(request,id):
    task=forms.TaskForm()
    list=get_object_or_404(List,id=id)
    tasks=Task.objects.filter(lists=list)
    if request.method=='POST':
        task=forms.TaskForm(request.POST)
        if task.is_valid():
            instance=task.save(commit=False)
            instance.user=request.user
            instance.lists=list
            instance.save()
            return redirect('tasks:listdetail',id=list.id)
    context={'task':task,
    'tasks':tasks
    }
    return render(request,'listdetail.html',context)
@login_required()
def deletetask(request,id):
    task=Task.objects.get(id=id)
    list_id=task.lists.id
    if request.user== task.user:
        task.delete()
        return redirect('tasks:listdetail', id=list_id)
    return HttpResponse('request user listin sahibi deyil')
@login_required()
def updatetask(request,id):
    task=get_object_or_404(Task,id=id)
    taskform=forms.TaskForm(instance=task)
    if request.method=='POST':
        taskform=forms.TaskForm(request.POST,instance=task)
        if taskform.is_valid():
            taskform.save()
            return redirect('tasks:listdetail', id=task.lists.id)
    context={
        'task':task,
        'taskform':taskform
    }
    return render(request,"updatetask.html",context)

@login_required()
def updatelist(request,id):
    list=get_object_or_404(List,id=id)
    listform=forms.ListForm(instance=list)
    if request.method=='POST':
        listform=forms.ListForm(request.POST,instance=list)
        if listform.is_valid():
            listform.save()
            return redirect('tasks:home')
    context={
        'list':list,
        'listform':listform
    }
    return render(request,'updatelist.html',context)


