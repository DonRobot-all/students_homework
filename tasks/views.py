from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    # return HttpResponse("Главная страница")
    return render(request, 'tasks/index.html')

def task_list(request):
    # return HttpResponse("Привет! Это список заданий")
    # return render(request, 'tasks/task_list.html')
    # tasks = ['Сделать уроки', 'Прочитать книгу', 'Помыть посуду']
    tasks = [
        {'title': 'Сделать уроки',    'description': 'Математика и русский'},
        {'title': 'Прочитать книгу',  'description': 'Глава 3 и 4'},
        {'title': 'Написать код',    'description': 'Django проект'},
    ]
    return render(request, 'tasks/task_list.html', {'tasks': tasks})

def news(request, pk):
    return HttpResponse(f"Проверка страница {pk}")


def task_detail(request, pk):
    tasks = [
        {'title': 'Сделать уроки',    'description': 'Математика и русский'},
        {'title': 'Прочитать книгу',  'description': 'Глава 3 и 4'},
        {'title': 'Написать код',    'description': 'Django проект'},
    ]
    task = tasks[pk - 1]   # pk с 1, список с 0
    return render(request, 'tasks/task_detail.html', {'task': task, 'pk': pk})