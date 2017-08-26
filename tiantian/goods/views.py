# -*- coding: utf-8 -*-
from django.shortcuts import render
from .models import  GoodsInfo,GoodsInfo
from django.http import HttpResponse

def index(request):
    return render(request,'index.html')

