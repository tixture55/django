
from __future__ import unicode_literals

# -*- coding: utf-8 -*-
import io
import os
from django.conf import settings
from django.views import generic
from django.http import HttpResponse
from django.template.loader import get_template
from django.db import models
from blog.models import Member
from django.shortcuts import render
from . import forms

# Create your views here.

class MemberListView(generic.ListView):
    model = Member

    def items(self):
        return Member.objects.filter(user=self.request.user)


def login_required():
    def preprocess(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            request = args[0]

            if not request.session.get('logged_in'):
                raise Http404

            return func(*args, **kwargs)
        return wrapper
    return preprocess


def post_list(request):
    return render(request, 'blog/post_list.html', {})


def hello_forms(request):
    form = forms.HelloForm(request.GET or None)
    if form.is_valid():
        message = 'data inspection is success!'
    else:
        message = 'data inspection is failed!'
   
    if request.user.is_authenticated():
        text_list = [obj.name for obj in Member.objects.all()]
        #return Member.objects.filter(name = 'mike')
        #return text_list
    else:
        message = 'ta inspection is failed!'

 
    d = {
        'form': form,
        'message': message,
        'text_list': text_list,
    }
    return render(request, 'forms.html', d)

def hello_template(request):
    return render(request, 'index.html')

def hello_get_query(request):
    d = {
        'your_name': request.GET.get('your_name')
    }
    return render(request, 'get_query.html', d)
