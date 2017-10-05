# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse

from .models import Users, Messages, Comments

# Create your views here.
def index(request):
    a = 'it works'
    return HttpResponse("ok")
