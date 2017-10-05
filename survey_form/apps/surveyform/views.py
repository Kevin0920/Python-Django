# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect

# Create your views here.

def index(request):

    return render(request,'surveyform/index.html')


def proccess(request):
    if request.method == "POST":
        request.session['name'] = request.POST['name'],
        request.session['location'] = request.POST['location'],
        request.session['language'] = request.POST['language'],
        request.session['comment'] = request.POST['comment']

    elif request.method == "GET":
        return redirect("/")

    return redirect('/result')

def result(request):
        result_data = {
            'name': request.session['name'][0],
            'location': request.session['location'][0],
            'language': request.session['language'][0],
            'comment': request.session['comment']
        }

        return render(request, 'surveyform/result.html', result_data)
