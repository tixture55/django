# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse('Hello World from Polls')
def edit(request):
    return HttpResponse('編集')

def show(request):
    return HttpResponse('読む')
