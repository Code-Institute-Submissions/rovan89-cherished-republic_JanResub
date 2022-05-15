from django import forms
from .models import Comment, Post


class CommentForm(forms.ModelForm):
    """
    This is the for for user comments.
    It class inherits from the Comment class in models.py
    """

    class Meta:
        model = Comment
        fields = ('body',)


class UserPostForm(forms.ModelForm):
    """
    This is the form for user posts.
    It class inherits from the Comment class in models.py
    """
    class Meta:
        model = Post
        fields = ['title', 'content', 'author']
