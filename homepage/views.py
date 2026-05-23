from django.shortcuts import render

def index(request):
    # return HttpResponse("Главная страница")
    return render(request, 'tasks/index.html')