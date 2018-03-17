
from __future__ import unicode_literals

# -*- coding: utf-8 -*-
import io
import os
from django.conf import settings
from django.views import generic
from django.http import HttpResponse
from django.template.loader import get_template

from django.shortcuts import render

# Create your views here.

def post_list(request):
    return render(request, 'blog/post_list.html', {})
