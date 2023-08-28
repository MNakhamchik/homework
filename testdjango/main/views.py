from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm


def index(request):
    tasks = Task.objects.order_by('-id')
    return render(request, 'main/index.html', {'title': 'главная страница', 'task': tasks})


def about(request):
    return render(request, 'main/about.html')


def create(request):
    error = ''
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'Произошла ошибка'

    form = TaskForm()
    context = {
        'form': form,
        'error': error
    }
    return render(request, 'main/create.html', context)


def delete(request, pk):
    tasks = Task.objects.get(pk=pk)
    if request.method == 'POST':
        tasks.delete()
        return redirect('home')
    return render(request, 'main/delete.html')


def update(request, pk):
    error = ''
    tasks = Task.objects.get(pk=pk)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=tasks)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'Произошла ошибка'

    form = TaskForm()
    context = {
        'form': form,
        'error': error
    }
    return render(request, 'main/update.html', context)