# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-10 07:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library_app', '0006_auto_20170309_2008'),
    ]

    operations = [
        migrations.AddField(
            model_name='present_book',
            name='attribute',
            field=models.CharField(default='present', max_length=20),
        ),
        migrations.AddField(
            model_name='present_book',
            name='comment',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='request_book',
            name='attribute',
            field=models.CharField(default='request', max_length=20),
        ),
        migrations.AddField(
            model_name='request_book',
            name='comment',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
