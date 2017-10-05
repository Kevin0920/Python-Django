# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from .models import Blog, Comment, User

# Create your views here.
def index(request):
    User.userManager.login('mail@gmail.com','password')

    context = {
        'blogs':Blog.objects.all()
        # 'comments':Comment.object.all().filter()
    }
    return render(request, 'blog/index.html',context)

def blogs(request):
    # Using ORM
    Blog.objects.create(title=request.POST['title'], post=request.POST['post'])
    #
    return redirect('/')

def comments(request, id):
    blog = Blog.objects.get(id=id)
    Comment.objects.create(comment=request.POST['comment'],blog=blog)

    return redirect('/')
