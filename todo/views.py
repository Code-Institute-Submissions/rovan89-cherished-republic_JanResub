from django.shortcuts import render, get_list_or_404
from django.views import generic
from .models import ToDoList


class TaskList(generic.ListView):
    model = ToDoList
    queryset = ToDoList.objects.order_by('-created_on')
    template_name = 'todo_list.html'
    paginate_by = 6


class TodoItems(generic.ListView):

    def get(self, request, *args, **kwargs):
        queryset = ToDoList.objects.filter()
        todo_item = get_list_or_404(queryset)

        return render(
            request,
            "todo/todo_list.html",
            {
                "todo_item": todo_item,
            },
        )
