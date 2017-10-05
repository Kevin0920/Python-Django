# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect

# Create your views here.

def index(request):
    return render(request, 'dninjas/index.html')
def ninjas(request):
    return render(request, 'dninjas/ninjas.html')

def colorpicked(request, color):
        if color == 'orange':
            return render(request, 'dninjas/michelangelo.html')
        elif color == 'red':
            return render(request, 'dninjas/raphael.html')
        elif color == 'purple':
            return render(request, 'dninjas/donatello.html')
        elif color == 'blue':
            return render(request, 'dninjas/leonardo.html')
        else:
            return render(request, 'dninjas/granny.html')
