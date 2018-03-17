from django.conf.urls import include, url
from . import views

urlpatterns = [
    #url(r'^$', views.post_list, name='post_list'),
    #url(r'^sample$', SampleTemplateView.as_view()),
    url(r'^', views.post_list, name='post_list'),
    url(r'^/members/$', views.index, name='index'),
]
