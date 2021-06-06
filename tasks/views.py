from django.shortcuts import render
from django.views.generic import ListView
from .models import Tasks

def home_page(request):
    return render(request, 'base.html')


def task_page(request):
    return render(request, 'pages/tasks.html')


class TaskPage(ListView):
    queryset = Tasks.objects.all()
    context_object_name = 'tasks'
    template_name = 'pages/tasks.html'

# class PostListView(ListView):
#     queryset = Post.published.all()
#     context_object_name = 'posts'
#     paginate_by = 3
#     template_name = 'blog/post/list.html'
