# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-10 07:56
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('library_app', '0007_auto_20170310_1651'),
    ]

    operations = [
        migrations.RenameField(
            model_name='present_book',
            old_name='link',
            new_name='book_link',
        ),
    ]
