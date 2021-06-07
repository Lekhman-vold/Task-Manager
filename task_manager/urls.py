from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('my-tasks/', admin.site.urls),
    path('', include('tasks.urls')),
    path('auth_app/', include('auth_app.urls')),

]
