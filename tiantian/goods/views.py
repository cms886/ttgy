# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
from .models import TypeInfo,GoodsInfo
def index(request):
    #商品类
    goods = TypeInfo.objects.all().order_by()[:6]  # 取出最新信息前4条
    #商品名称
    post_list = GoodsInfo.objects.all().order_by('-gtime')[:4]   #取出最新信息前4条
    return render(request,'index.html',context={'post_list':post_list,'goods':goods})

def detail(request):
    return render(request,'detail.html')
