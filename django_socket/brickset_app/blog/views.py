
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

def post_list(request):
    return render(request, 'blog/post_list.html', {})


def hello_forms(request):
    form = forms.HelloForm(request.GET or None)
    if form.is_valid():
        message = 'data inspection is success!'
    else:
        message = 'data inspection is failed!'
    d = {
        'form': form,
        'message': message,
    }
    return render(request, 'forms.html', d)

def hello_template(request):
    return render(request, 'index.html')

def hello_get_query(request):
    d = {
        'your_name': request.GET.get('your_name')
    }
    return render(request, 'get_query.html', d)
