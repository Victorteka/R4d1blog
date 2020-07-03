from django.conf.urls import url
from . import views

urlpatterns = [
    url('^$', views.all_blog_posts, name='posts')
]
