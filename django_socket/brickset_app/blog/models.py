# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Customer(models.Model):
    # id = AutoField(primary_key=True)  # 自動的に追加されるので定義不要
    last_name = models.CharField(max_length=20)
    first_name = models.CharField(max_length=20)
    email_address = models.EmailField(max_length=255, unique=True)
    memo = models.TextField(null=True)



class Member(models.Model):
    name = models.CharField('氏名', max_length=255)
    email = models.CharField('E-Mail', max_length=255)
    age = models.IntegerField('年齢', blank=True, default=0)
    created_at = models.DateTimeField()

    def __str__(self):
        return self.name

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


class Question(models.Model):
    title = models.CharField(max_length=100)
    text = models.CharField(max_length=1000)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
