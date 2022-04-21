from . import views
from django.urls import path, include

urlpatterns = [
    path('', views.taskList.as_view(), name="mainTask")
]
