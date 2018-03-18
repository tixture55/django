
from __future__ import unicode_literals

# -*- coding: utf-8 -*-
import io
import os
from django.conf import settings
from django.views import generic
from django.http import HttpResponse
from django.template.loader import get_template
from django.db import models
from django.db.models import Prefetch
from blog.models import Member
from django.shortcuts import render

# Create your views here.

class MemberListView(generic.ListView):
    model = Member

    def items(self):
        return Member.objects.filter(user=self.request.user)

def post_list(request):
    return render(request, 'blog/post_list.html', {})
