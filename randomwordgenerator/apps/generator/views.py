# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import os, binascii # include this at the top of your file
from django.shortcuts import render, redirect



# Create your views here.
def index(request):

    if 'randomnumber' in request.session:
        pass
    elif 'attempt' in request.session:
        pass
    else:
        request.session['attempt'] = 1
        request.session['randomnumber'] = binascii.b2a_hex(os.urandom(14))

    return render(request, 'generator/index.html')

def generate(request):
    request.session['randomnumber'] = binascii.b2a_hex(os.urandom(14))
    request.session['attempt'] += 1

    return redirect("/")
