from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Category(models.Model):
    '''Model for category's for tasks'''

    name = models.CharField(max_length=256, unique=True)

    def __str__(self):
        return self.name


class Task(models.Model):
    '''Model for tasks'''

    title = models.CharField(max_length=256, blank=False)
    description = models.TextField(blank=True)
    posted_date = models.DateTimeField(auto_now_add=True)
    deadline_date = models.DateField(blank=False)
    completed = models.BooleanField(default=False)
    category = models.ForeignKey(to=Category, on_delete=models.CASCADE)
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.title}: {self.deadline_date}, {self.completed}'
