from django.db import models


STATUS = ((0, "Todo"), (1, "In Progress"), (2,"Completed"))

class ToDoList(models.Model):
    title = models.CharField(max_length=100, unique=True)
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    content = models.TextField()

    def __str__(self):
        return self.title