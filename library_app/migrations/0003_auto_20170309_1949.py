# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-09 10:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library_app', '0002_auto_20170309_1816'),
    ]

    operations = [
        migrations.AddField(
            model_name='request_book',
            name='isbn',
            field=models.IntegerField(default=9784774142357, verbose_name='isbn_code here'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='request_book',
            name='link',
            field=models.CharField(default='http://iss.ndl.go.jp/books/R100000002-I000010835519-00', max_length=200),
            preserve_default=False,
        ),
    ]