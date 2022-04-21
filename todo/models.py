from django.db import models


class ToDoList(models.Model):
    title = models.CharField(max_length=100, unique=True)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title