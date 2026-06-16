from django.shortcuts import render, redirect
from django.http import HttpResponse

from .models import Task
from .forms import TaskForm

# Create your views here.

def index(request):
    # return HttpResponse("Главная страница")
    return render(request, 'tasks/index.html')

def task_list(request):
    # return HttpResponse("Привет! Это список заданий")
    # return render(request, 'tasks/task_list.html')
    # tasks = ['Сделать уроки', 'Прочитать книгу', 'Помыть посуду']
    # tasks = [
    #     {'title': 'Сделать уроки',    'description': 'Математика и русский'},
    #     {'title': 'Прочитать книгу',  'description': 'Глава 3 и 4'},
    #     {'title': 'Написать код',    'description': 'Django проект'},
    # ]
    # return render(request, 'tasks/task_list.html', {'tasks': tasks})
    tasks = Task.objects.all()
    return render(request, 'tasks/task_list.html', {'tasks': tasks})
    
def news(request, pk):
    return HttpResponse(f"Проверка страница {pk}")


def task_detail(request, pk):
    # tasks = [
    #     {'title': 'Сделать уроки',    'description': 'Математика и русский'},
    #     {'title': 'Прочитать книгу',  'description': 'Глава 3 и 4'},
    #     {'title': 'Написать код',    'description': 'Django проект'},
    # ]
    # task = tasks[pk - 1]   # pk с 1, список с 0
    # return render(request, 'tasks/task_detail.html', {'task': task, 'pk': pk})
    task = Task.objects.get(pk=pk)
    return render(request, 'tasks/task_detail.html', {'task': task, 'pk': pk})


def task_create(request):
    if request.method == 'POST':          # пользователь нажал "Сохранить"
        form = TaskForm(request.POST)
        if form.is_valid():               # данные прошли проверку
            form.save()                   # сохранить в БД
            return redirect('task_list')  # перейти к списку
    else:                                 # пользователь просто открыл страницу
        form = TaskForm()

    return render(request, 'tasks/task_create.html', {'form': form})