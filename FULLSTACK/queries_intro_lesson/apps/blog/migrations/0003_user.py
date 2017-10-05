# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-21 02:33
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20170621_0044'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=45)),
                ('last_name', models.CharField(max_length=45)),
                ('password', models.CharField(max_length=100)),
                ('created_at', models.DateField(auto_now_add=True)),
                ('updated_at', models.DateField(auto_now=True)),
            ],
            managers=[
                ('userManager', django.db.models.manager.Manager()),
            ],
        ),
    ]
