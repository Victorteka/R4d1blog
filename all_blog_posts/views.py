from django.shortcuts import render
from django.views.generic import DetailView
import requests

from .models import Post

# Create your views here.


def all_blog_posts(request):
    posts = Post.objects.all()
    news = get_news()
    return render(request, 'all_blog_posts.html', {"posts": posts, "news": news})


class PostDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'

# get cyber security articles


def get_news():
    url = 'https://newsapi.org/v2/everything?q=cyber%20security&apiKey=14ae627890954195922391f40adfdf58'
    r = requests.get(url)
    news = r.json()
    news_list = news['articles']
    return news_list
