from django.conf.urls import include, url
from . import views
from django.views.generic import ListView

urlpatterns = [
    #url(r'^$', views.post_list, name='post_list'),
    url(r'^template/$', views.hello_template, name='hello_template'),
    url(r'^get/$', views.hello_get_query, name='hello_get_query'), 
    url(r'^$', views.hello_forms, name='hello_forms'),
]
