# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-03-17 21:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_member'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_name', models.CharField(max_length=20)),
                ('first_name', models.CharField(max_length=20)),
                ('email_address', models.EmailField(max_length=255, unique=True)),
                ('memo', models.TextField(null=True)),
            ],
        ),
    ]
