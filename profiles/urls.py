from django.urls import path
from . import views

urlpatterns = [
    path('<int:pk>/', views.UpdateUserProfileView.as_view(), name="update_profile"),
    path('delete_profile/<int:pk>', views.DeleteProfileView.as_view(), name="delete_profile"),
]