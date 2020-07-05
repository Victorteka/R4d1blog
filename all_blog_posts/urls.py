from django.conf.urls import url
from django.urls import path


from . import views
from .views import PostDetailView

urlpatterns = [
    url('^$', views.all_blog_posts, name='posts'),
    path('<int:pk>/cyber-security-content',
         PostDetailView.as_view(),
         name='detail'),
]
