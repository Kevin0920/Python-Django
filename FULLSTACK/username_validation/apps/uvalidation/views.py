# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages

from .models import Users
# Create your views here.
def index(request):
    context = {
        'allusers': Users.objects.all()
    }
    if request.method == "POST":
        if len(request.POST['name']) < 8:
            messages.add_message(request, messages.ERROR, 'Invalid input: please enter string at least 8 characters')
        elif len(request.POST['name']) > 28:
            messages.add_message(request, messages.ERROR, 'Invalid input: please enter string less 28 characters')
        else:
            if len(Users.objects.filter(name=request.POST['name'])) > 0:
                messages.add_message(request, messages.ERROR, 'Invalid input: we already added this name in DB')
            else:
                newuser = Users(name=request.POST['name'])
                newuser.save()
                messageSuccess = 'The user you have entered ' + str(request.POST['name']) +' is valid, Thank you!'
                messages.add_message(request, messages.SUCCESS, messageSuccess)
                return redirect('/success')
    else:
        pass
    return render(request,'uvalidation/index.html',context)


def success(request):
    context = {
        'allusers': Users.objects.all()
    }
    if request.method == "POST":
        if request.POST['delete'] =='yes':
            Users.objects.filter(id=request.POST['id']).delete()
    else:
        pass
    return render(request,'uvalidation/success.html',context)
