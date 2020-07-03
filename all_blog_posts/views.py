from django.shortcuts import render

# Create your views here.


def all_blog_posts(request):
    return render(request, 'all_blog_posts.html')
