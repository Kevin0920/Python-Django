# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect

from .models import People
# Create your views here.

def index(request):
    People.objects.create(first_name="Mike",last_name="Hannon")
    people = People.objects.all()
    print people
    return render(request, 'test_app/index.html')
