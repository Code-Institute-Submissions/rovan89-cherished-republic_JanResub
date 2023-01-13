from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy
from django.views.generic.edit import UpdateView, DeleteView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.models import User

from .models import Profile


class UpdateUserProfileView(SuccessMessageMixin, UpdateView):
    """ View to update user profiles """
    model = Profile
    template_name = 'update_profile.html'
    success_message = "Your post was updated successfuly!"
    fields = ('first_name', 'last_name', 'bio', 'email', 'phone_number')
    success_url = reverse_lazy('home')


class DeleteProfileView(SuccessMessageMixin, DeleteView):
    """ View to delete profile """
    model = User
    template_name = "delete_profile.html"
    success_message = "User profile has been deleted"
    success_url = reverse_lazy('home')
