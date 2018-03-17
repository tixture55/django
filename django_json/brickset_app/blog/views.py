
from __future__ import unicode_literals

# -*- coding: utf-8 -*-
import io
import os
from django.conf import settings
from django.http import HttpResponse
from django.template.loader import get_template

from django.shortcuts import render

from blog.models import Member

# Create your views here.

def post_list(request):
    return render(request, 'blog/post_list.html', {})

def index(request):
    members = Member.objects.all().order_by('id') 
    return render(request, 'members/index.html', {'members':members}) 
