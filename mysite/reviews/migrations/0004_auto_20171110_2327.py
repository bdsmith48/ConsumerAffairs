# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-11 05:27
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0003_auto_20171110_2327'),
    ]

    operations = [
        migrations.RenameField(
            model_name='review',
            old_name='ating',
            new_name='rating',
        ),
    ]
