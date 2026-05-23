from django.urls import path
from . import views

urlpatterns = [
    path('', views.task_list, name='task_list'),
    path('<int:pk>/', views.task_list_int, name='task_list_int'),
    path('news/<pk>/', views.news, name='news'),
    
]