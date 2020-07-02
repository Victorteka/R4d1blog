from django.conf.urls import url
from . import views

urlpatterns = [
    url('^$', views.landing_page, name='home_page')
]
