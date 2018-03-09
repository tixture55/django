# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render #追加する


# Create your views here.

def home(request):
    return HttpResponse("Hello, Django World")

def hello_template(request):
    return render(request, 'index.html')


