from django.contrib import admin
from .models import Tasks


@admin.register(Tasks)
class TasksAdmin(admin.ModelAdmin):
    list_display = ['title', 'status', 'start_date', 'end_date']
    list_filter = ['status']

# @admin.register(ImageUser)
# class ImageUserAdmin(admin.ModelAdmin):
#     list_display = ['user', 'image']
