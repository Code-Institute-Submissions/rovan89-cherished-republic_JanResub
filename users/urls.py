from django.urls import path
from blog import views as blog_views
from . import views


urlpatterns = [
    path('register/', views.register, name='register'),
    path('', blog_views.PostList.as_view(), name="home"),
]
