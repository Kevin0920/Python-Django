# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .models import Product
# Create your views here.
def index(request):
    Product.objects.create(name="Razor",description="Gilette super blade",weight=0.05,price=10,cost=8,category="razors")
    Product.objects.create(name="Razor Bic",description="Bic nice blade",weight=0.05,price=10,cost=8,category="razors")
    Product.objects.create(name="Razor knife",description="Knife super blade",weight=0.05,price=10,cost=8,category="razors")
    products = Product.objects.all()
    log = []
    for key in products:
        log += [str(key.name) + ": " + str(key.description) + " " + str(key.weight) + " " + str(key.price)]

    transdata = {
        "show":log
    }
    print log
    return render(request, 'product/index.html',transdata)
