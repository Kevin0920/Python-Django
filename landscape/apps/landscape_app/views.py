# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,redirect
import random
# Create your views here.
def index(request):
    return render(request, 'landscape_app/index.html')


def idroute(request, id):
    transdata = {
        'id': id,
        'landscape':'default'
    }
    intid = int(id)
    randomnumber = str(random.randrange(1,11))
    if intid == 0:

        return render(request, 'landscape_app/error.html')
    # • 1-10: A landscape with snow
    elif intid > 0 and intid <=10:
        transdata['landscape'] = 'snow/'+ randomnumber +'.jpeg'
    # • 11-20: A landscape in the desert
    elif intid > 10 and intid <=20:
        transdata['landscape'] = 'desert/'+ randomnumber +'.jpeg'
    # • 21-30: A landscape in a forest
    elif intid > 20 and intid <=30:
        transdata['landscape'] = 'forest/'+randomnumber+'.jpeg'
    # • 31-40: A landscape in a vineyard
    elif intid > 30 and intid <=40:
        transdata['landscape'] = 'vineyard/'+randomnumber+'.jpeg'
    # • 41-50: A tropical landscape
    elif intid > 40 and intid <=50:
        transdata['landscape'] = 'tropical/'+randomnumber+'.jpeg'
    else:
        return render(request, 'landscape_app/error.html')


    return render(request, 'landscape_app/result.html', transdata)


def error(request):

    return render(request, 'landscape_app/error.html')
