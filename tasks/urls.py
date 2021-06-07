from django.urls import path
from . import views

app_name = 'tasks'

urlpatterns = [
    path('', views.home_page, name='home_page'),
    path('tasks/', views.TaskPage.as_view(), name='task_page'),
    path('update-task/<int:pk>/', views.UpdateTask.as_view(), name='update_task')
]
