from django.shortcuts import render
from django.views.generic import DetailView

from .models import Post

# Create your views here.


def all_blog_posts(request):
    posts = Post.objects.all()
    return render(request, 'all_blog_posts.html', {"posts": posts})


class PostDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'
