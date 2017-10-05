# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect

import random, time

# Create your views here.
def index(request):


    if 'score' in request.session and 'log' in request.session:
        pass
    else:
        request.session['score'] = 0
        request.session['log'] = []
    return render(request, 'ninjagold/index.html')

def process_money(request):


    if request.method == "POST":
        if request.POST['activity'] == 'farm':
            number = random.randrange(9,21)
            message = "Earned " + str(number) + " golds from the farm (" + time.strftime('%Y/%d/%m %l%:%M%p') + ")"

            request.session['score'] += number
            request.session['log'].insert(0, message)

        if request.POST['activity'] == 'cave':
            number = random.randrange(4,11)
            message = "Earned " + str(number) + " golds from the farm (" + time.strftime('%Y/%d/%m %l%:%M%p') + ")"

            request.session['score'] += number
            request.session['log'].insert(0, message)
        if request.POST['activity'] == 'house':
            number = random.randrange(1,6)
            message = "Earned " + str(number) + " golds from the farm (" + time.strftime('%Y/%d/%m %l%:%M%p') + ")"

            request.session['score'] += number
            request.session['log'].insert(0, message)
        if request.POST['activity'] == 'casino':
            number = random.randrange(-51,51)
            if number >0:
                message = "Earned " + str(number) + " golds from the farm (" + time.strftime('%Y/%d/%m %l%:%M%p') + ")"
            else:
                message = "Entered a casino and lost  " + str(number) + " golds... Ouch... (" + time.strftime('%Y/%d/%m %l%:%M%p') + ")"

            request.session['score'] = request.session['score'] + number
            request.session['log'].insert(0, message)
        if request.POST['activity'] == 'reset':
            request.session['score'] = 0
            request.session['log'] = []
    else:
        return redirect('/')

    return redirect('/')
