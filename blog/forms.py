from .models import Comment
from django import forms

class CommentForm(forms.ModelForm):
    """
    This class is the model for users comments.
    It inherits from the Comment class in models.py
    """
    class Meta:
        model = Comment
        fields = ('body',)