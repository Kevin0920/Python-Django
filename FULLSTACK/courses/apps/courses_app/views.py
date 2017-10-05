# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect, HttpResponse
from .models import Courses
# Create your views here.
def index(request):
    context = {
        "courses":Courses.objects.all()
    }
    return render(request, 'courses_app/index.html',context)


def add(request):
    newRecord = Courses(
        name=request.POST['name'],
        description=request.POST['description'])
    newRecord.save()
    return redirect('/')


def destroy(request, id):
    if request.method == "POST":
        print request.POST['delete']
        Courses.objects.filter(id=id).delete()
        return redirect('/')
    else:
        if len(Courses.objects.filter(id=id)) > 0:
            query = Courses.objects.get(id=id)
            context = {
                'name':query.name,
                'description':query.description,
                'id':id
            }

            return render(request, 'courses_app/confirm.html', context)
        else:
            pass
    return HttpResponse("<h1>Sorry, we don't have this record in DataBase</h1>")
