from django.db import models
from django.contrib.auth.models import User


class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    title = models.CharField(max_length=200)
    category = models.CharField(max_length=200)
    due_date = models.DateTimeField(null=True, blank=True)
    done = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['done']
