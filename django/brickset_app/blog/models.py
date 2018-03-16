# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)


class Article(models.Model):
    title = models.CharField(max_length=100)
    text = models.CharField(max_length=1000)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)



class Hello(models.Model):
    your_name = models.CharField(max_length=10)

    def __str__(self):
        return "<{0}>".format(self.your_name)
