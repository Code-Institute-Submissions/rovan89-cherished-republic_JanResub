from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from .models import ToDoList


class TaskList(generic.ListView):
    model = ToDoList
    queryset = ToDoList.objects.order_by('-created_on')
    template_name = 'todo_list.html'



