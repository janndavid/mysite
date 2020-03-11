# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader

# Create your views here.

# Dette er den nemme måde at gøre det på
def index(request):
    return render(request,'polls/index.html')
