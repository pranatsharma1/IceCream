# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-07-29 21:23
from __future__ import unicode_literals

from django.db import migrations, models

import Core.models


class Migration(migrations.Migration):
    dependencies = [
        ('Core', '0010_project_image_path'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='pic_path',
            field=models.FileField(default=None, null=True,
                                   upload_to=Core.models.upload_location),
        ),
        migrations.AlterField(
            model_name='project',
            name='image_path',
            field=models.FileField(default=None, null=True,
                                   upload_to=Core.models.upload_location),
        ),
    ]
