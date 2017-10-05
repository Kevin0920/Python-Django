# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from .models import Book

# Create your views here.
def index(request):
    print Book.objects.all()
    return render(request,"book_model/index.html")
