from django.conf.urls import include, url
from . import views
from django.views.generic import ListView

urlpatterns = [
    #url(r'^$', views.post_list, name='post_list'),
    url(r'^', views.post_list, name='post_list'),
    #url(r'^items/$', ListView.as_view()),
]
