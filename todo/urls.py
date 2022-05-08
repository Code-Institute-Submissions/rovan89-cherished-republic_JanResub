from . import views
from django.urls import path

urlpatterns = [
    path('todo_list/', views.TodoItems.as_view(), name='todo_list'),
    #path('todo/', views.ToDoList.as_view, name="todo_list"),
]
