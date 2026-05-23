from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    # return HttpResponse("Главная страница")
    return render(request, 'tasks/index.html')

def task_list(request):
    # return HttpResponse("Привет! Это список заданий")
    # return render(request, 'tasks/task_list.html')
    tasks = ['Сделать уроки', 'Прочитать книгу', 'Помыть посуду']
    return render(request, 'tasks/task_list.html', {'tasks': tasks})

def task_list_int(request, pk):
    return HttpResponse(f"Страница задания {pk}")


def news(request, pk):
    return HttpResponse(f"Проверка страница {pk}")