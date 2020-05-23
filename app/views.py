# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
def landing(request):
    return render (request, 'buyer/buyer_index.html', {})

def car_listing(request):
    return render (request, 'buyer/car_listing.html', {})

def car_details(request):
    return render (request, 'buyer/view_car.html', {})

def blog_list(request):
    return render (request, 'buyer/blog_list.html', {})