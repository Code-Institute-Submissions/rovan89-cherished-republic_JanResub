from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class NewUserForm(UserCreationForm):
    """
    This class has customised the UserCreationForm.
    The four user inputs are 'username', 'email', 'password1', 'password2'
    Password1 is validated by retyping it into password2).
    """
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
