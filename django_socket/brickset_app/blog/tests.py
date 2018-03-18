# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase
from django.utils import timezone

from .models import Question

# Create your tests here.

class BlogTest(TestCase):
    def test_hoge(self):
        print('test!')

class BlogTimezoneTest(TestCase):
    def test_was_published_recently(self):
        obj = Question(pub_date=timezone.now())
        self.assertTrue(obj.was_published_recently())
