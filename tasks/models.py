from django.db import models
from django.contrib.auth.models import User


class Tasks(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100, blank=True)
    text = models.TextField(blank=True)
    url = models.URLField(blank=True)
    status = models.BooleanField(default=False)
    start_date = models.DateTimeField(auto_now_add=True)
    end_date = models.DateTimeField(auto_now=False, blank=True)

    def __str__(self):
        return f"Task: {self.title}"
