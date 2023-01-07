from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy
from django.views.generic.edit import UpdateView, DeleteView

from .models import Profile


class UpdateUserProfileView(UpdateView):
    """ View to update user profiles """
    model = Profile
    template_name = 'update_profile.html'
    fields = '__all__'
    success_url = reverse_lazy('home')


