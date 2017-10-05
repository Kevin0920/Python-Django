# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# our manager:
class UserManager(models.Manager):
    def login(self,email,password):
        print "just logined"
        pass
    def register(self,email,password,first_name,last_name):
        print 'just registered'
        pass

class User(models.Model):
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    password = models.CharField(max_length=100)

    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    userManager = UserManager()

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=100)
    post = models.TextField(max_length=1000)

    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

class Comment(models.Model):
    blog = models.ForeignKey(Blog)
    comment = models.TextField(max_length=1000)

    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
