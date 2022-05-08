from django.db import models

STATUS = ((0, "Ongoing"), (1, "Completed"))

class ToDoList(models.Model):
    title = models.CharField(max_length=100, unique=True)
    created_on = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(max_length=250, unique=True, null=True)
    content = models.TextField()
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title
