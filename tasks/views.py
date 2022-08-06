from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm

from django.views.generic.list import ListView


# Create your views here.

def home(request):
    tasks = Task.objects.all()
    context = {"tasks": tasks}
    return render(request, 'tasks/home.html', context)


def details(request):
    context = {}
    return render(request, 'tasks/details.html', context)


def add_user(request):
    form = TaskForm()
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    context = {'form': form}
    return render(request, 'tasks/add_task.html', context)


def delete_task(request, pk):
    task = Task.objects.get(id=pk)
    if request.method == 'POST':
        task.delete()
        return redirect('home')
    context = {'task': task}
    return render(request, 'tasks/delete_task.html', context)


def edit_task(request, pk):
    task = Task.objects.get(id=pk)
    form = TaskForm(instance=task)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('home')
    context = {'task': task, 'form': form}
    return render(request, 'tasks/edit_task.html', context)