from django.db import models
from django.urls import reverse

from django.contrib.auth.models import User



class Profile(models.Model):
    """
    This a cumstom user profile class.
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, default='Enter your bio here')
    first_name = models.CharField(max_length=50, null=True, blank=True)
    last_name = models.CharField(max_length=50, null=True, blank=True)
    email = models.EmailField(max_length=254, null=True, blank=True)
    phone_number = models.CharField(max_length=12, null=True, blank=True)

    def __str__(self):
        return str(self.user)

