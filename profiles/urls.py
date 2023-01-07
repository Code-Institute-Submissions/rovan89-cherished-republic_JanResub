from django.urls import path
from . import views

urlpatterns = [
    path('<int:pk>/', views.UpdateUserProfileView.as_view(), name="update_profile"),
]