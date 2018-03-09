# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Person(models.Model):

   MAN = 0
   
   #名前
   name = models.CharField(max_length=128)
   #誕生日
   birthday = models.DateTimeField()

