# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
def index(request):

    return render(request, 'vinmyMVC/index.html')

def show(request):
    # print(request.method)
    return render(request, 'vinmyMVC/show_users.html')


def error(request):
    # print(request.method)
    return render(request, 'vinmyMVC/404.html')
