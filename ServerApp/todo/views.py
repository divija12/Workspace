from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponseRedirect, HttpResponse
from .models import *
from .forms import *

def todoappView(request):
    all_items = Task.objects.all()

    form = TaskForm()

    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/todo/')
    
    context = {'all_items': all_items, 'form': form}
    return render(request, 'todo/list.html', context)

def updateTask(request, new_name):
    task = Task.objects.get(id=new_name)
    form = TaskForm(instance=task)
    task.delete()  #deleting old instance of the task

    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
        return redirect('/todo/')
    
    context = {'form': form}
    return render(request, 'todo/update_task.html', context)

def deleteTask(request, id):
    item = Task.objects.get(id=id)
    item.delete()
    return redirect('/todo/')