# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Courses(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=250)

    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
