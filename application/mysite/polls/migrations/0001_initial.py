# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-06-21 05:54
from __future__ import unicode_literals

from django.db import migrations, models
import polls.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
                ('gender', models.CharField(choices=[('m', '\u7537'), ('f', '\u5973')], max_length=5)),
                ('avatar', models.ImageField(upload_to=polls.models.pic_upload_path)),
            ],
        ),
    ]
