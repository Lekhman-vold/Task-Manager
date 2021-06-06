from django.urls import path
from . import views

app_name = 'tasks'

urlpatterns = [
    path('', views.home_page, name='home_page'),
    path('tasks/', views.task_page, name='task_page'),
    path('test/', views.TaskPage.as_view())
]
