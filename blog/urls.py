from . import views
from django.urls import path, include

urlpatterns = [
    path('', views.PostList.as_view(), name="mainTask"),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
]
