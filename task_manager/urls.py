from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('my-tasks/', admin.site.urls),
    path('', include('tasks.urls')),
]
