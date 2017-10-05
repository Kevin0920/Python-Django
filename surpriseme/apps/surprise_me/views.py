# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
import random
VALUES = [
    '1 item', '2 item', '3 item', '4 item', '5 item', '6 item', '7 item', '8 item', '9 item', '10 item', '11 item', '12 item', 'Super item', '2','44','item lj','55',
    '44','555','indefinite item'
    ]
def shuffle(num):
    valength = len(VALUES)-1
    for i in range(0,len(VALUES)-1):
        randomindex = random.randrange(-1,valength)
        temp = VALUES[valength]
        VALUES[valength] = VALUES[randomindex]
        VALUES[randomindex] = temp
        # print "random index " + str(randomindex)

        valength = valength - 1

    return VALUES[:num]


# Create your views here.
def index(request):

    print shuffle(3)[0]
    return render(request, 'surprise_me/index.html')

def proccess(request):
    print request.method
    if request.method == "POST":
        print request.POST['number']
        if request.POST['number']:
            request.session['result']= shuffle(int(request.POST['number']))
        else:
            return redirect('/')
    else:
        return redirect("/")

    return redirect("/result")

def result(request):

    return render(request, 'surprise_me/result.html')
