# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect

# Create your views here.
def index(request):
    return render(request, 'realportfolio/index.html')
def projects(request):
    return render(request, 'realportfolio/projects.html')
def about(request):
    return render(request, 'realportfolio/about.html')
def testimotionals(request):
    return render(request, 'realportfolio/testimotionals.html')
def search(request):
    # print(request.method)
    'key' in request.session
    if request.method == "POST":
        print "*"*50
        print request.POST
        print request.method
        print "*"*50
        request.session['query'] = request.POST['query']
    return redirect("/")
