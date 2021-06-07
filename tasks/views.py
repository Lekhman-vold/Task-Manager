from django.shortcuts import render
from django.views.generic import ListView, UpdateView
from .models import Tasks
from .forms import TaskForm


def home_page(request):
    return render(request, 'base.html')


def task_page(request):
    return render(request, 'pages/tasks.html')


class TaskPage(ListView):
    queryset = Tasks.objects.all()
    context_object_name = 'tasks'
    template_name = 'pages/tasks.html'


class UpdateTask(UpdateView):
    model = Tasks
    template_name = 'pages/update_task.html'
    success_url = '/tasks/'
    fields = ['title', 'text', 'url']

    def get_context_data(self, **kwargs):
        context = super(UpdateTask, self).get_context_data(**kwargs)
        context['form'] = TaskForm()
        return context

# class PostListView(ListView):
#     queryset = Post.published.all()
#     context_object_name = 'posts'
#     paginate_by = 3
#     template_name = 'blog/post/list.html'
