#!coding:utf-8
from django.conf.urls import patterns, url
from polls import views

urlpatterns = patterns('',
        url(r'^$', views.show, name='show'),
        url(r'^edit/$', views.edit, name='edit'),
)
