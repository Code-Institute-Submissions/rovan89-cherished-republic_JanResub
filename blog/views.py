from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.contrib.auth.decorators import login_required
from django.views import generic, View
from django.http import HttpResponseRedirect
from django.utils.text import slugify
from django.contrib import messages
from .models import Post
from .forms import CommentForm, UserPostForm


class PostList(generic.ListView):
    """
    This class contains a list of user posts.
    The post are ordered by date of creation.
    The posts are filtered by thier status.
    """

    model = Post
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = "index.html"
    paginate_by = 6

@login_required 
def create_user_post(request):
    """
    This function allows a user to create a post,
    and updates the database.
    """
    form = UserPostForm()
    context = {
        'form': form
    }

    if request.method == 'POST':
        form = UserPostForm(request.POST)
        if form.is_valid():
            user_form = form.save(commit=False)
            user_form.slug = slugify(user_form.title)
            user_form.save()
            messages.success(request, "Your post was created successfully")
            return redirect('home')
    return render(request, "create_post.html", context)


def update_user_post(request, post_id):
    """
    This function allows the user to update a post.
    """
    post = get_object_or_404(Post, id=post_id)

    if request.method == 'POST':
        form = UserPostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            messages.success(request, "Your post was updated successfully")
            return redirect('home')
    form = UserPostForm(instance=post)
    context = {
        'post_author': post.author,
        'form': form
    }
    return render(request, 'update_post.html', context)


def delete_post(request, post_id):
    """
    This is the fuction for a user to delete a post.
    """

    post = get_object_or_404(Post, id=post_id)
    post.delete()
    messages.success(request, "Your post was deleted successfully")
    return redirect('home')


class PostDetail(View):
    """
    This view shows the post in full detail.
    It uses the get method to display the post.
    This also checks if a logged in user has liked the post.
    From forms.py the class uses CommentForm class to create a user comment.

    """

    def get(self, request, slug):
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approved=True).order_by('-created_on')
        liked = False

        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        return render(
            request,
            "post_detail.html",
            {
                "post": post,
                "comments": comments,
                "commented": False,
                "liked": liked,
                "comment_form": CommentForm()
            },
        )

    def post(self, request, slug):
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approved=True).order_by('-created_on')
        liked = False

        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        comment_form = CommentForm(data=request.POST)

        if comment_form.is_valid():
            comment_form.instance.email = request.user.email
            comment_form.instance.name = request.user.username
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.save()
            messages.info(request, "Your comment is awaiting approval")
        else:
            comment_form = CommentForm()

        return render(
            request,
            "post_detail.html",
            {
                "post": post,
                "comments": comments,
                "commented": True,
                "liked": liked,
                "comment_form": CommentForm()
            },
        )


class PostLike(View):
    """
    This class alllows users to like posts.
    """
    def post(self, request, slug):
        post = get_object_or_404(Post, slug=slug)

        if post.likes.filter(id=request.user.id).exists():
            post.likes.remove(request.user)
        else:
            post.likes.add(request.user)

        return HttpResponseRedirect(reverse('post_detail', args=[slug]))


def post_search(request):
    """
    This function allows users to search published post.
    """
    if request.method == "POST":
        searched = request.POST['searched']
        posts = Post.objects.filter(title__icontains=searched)

        return render(request, 'search_posts.html', {
            'searched': searched,
            'posts': posts
        })
    else:
        return render(request, 'search_posts.html', {})
