from django.shortcuts import render
from django.views import generic
from .models import ToDoList
from django.http import HttpResponse

class taskList(generic.ListView):
    model = ToDoList
    template_name = 'todo-list.html'
