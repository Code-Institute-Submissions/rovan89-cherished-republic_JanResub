from django.urls import path
from blog import views as blog_views
from . import views


urlpatterns = [
    path('register/', views.register, name='register'),
    path('home/', blog_views.PostList.as_view(), name="home"),
]
