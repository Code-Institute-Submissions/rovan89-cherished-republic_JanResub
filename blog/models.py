from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django.urls import reverse

STATUS = ((0, "Draft"), (1, "Published"))


class Post(models.Model):
    """
    This is the model for a post.
    """
    title = models.CharField(max_length=250, unique=True)
    slug = models.SlugField(max_length=250, unique=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="blog_posts")
    created_on = models.DateTimeField(auto_now_add=True)
    featured_image = CloudinaryField('image', default='placeholder')
    content = models.TextField()
    updated_on = models.DateTimeField(auto_now=True)
    status = models.IntegerField(choices=STATUS, default=1)
    likes = models.ManyToManyField(User, related_name='blog_likes', blank=True)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title

    def __str__(self):
        return self.content

    def number_of_likes(self):
        return self.likes.count()

    def get_absolute_url(self):
        return reverse('home', args=(str(self.id)))


class Comment(models.Model):
    """
    This is the model for comments.
    """
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=100)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    likes = models.ManyToManyField(User, related_name='comment_likes')
    approved = models.BooleanField(default=False)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return f"Comment {self.body} by {self.name}"
