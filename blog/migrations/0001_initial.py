# -*- coding: utf-8 -*-
# Generated by Django 1.9.3 on 2016-03-03 14:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=100)),
                ('text', models.TextField()),
                ('date', models.DateTimeField(auto_now=True)),
                ('slug', models.SlugField()),
            ],
        ),
    ]
