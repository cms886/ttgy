# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
from .models import TypeInfo,GoodsInfo
def index(request):
    #商品类
    goods = TypeInfo.objects.all().order_by()[:6]  # 取出最新信息前6条
    #商品名称
    #post_list = GoodsInfo.objects.all().order_by('-gtime')[:4]   #取出最新信息前4条
    # 楼层
    p = TypeInfo.objects.all()[0]
    xxsg = p.goodsinfo_set.all().order_by('-gtime')[:4]
    #海鲜水产
    type = TypeInfo.objects.all()[1]
    hxsc = type.goodsinfo_set.all().order_by('-gtime')[:4]
    #猪肉 牛羊
    r = TypeInfo.objects.all()[2]
    zrny = r.goodsinfo_set.all().order_by('-gtime')[:4]
    #禽类蛋品
    dan = TypeInfo.objects.all()[3]
    qldp = dan.goodsinfo_set.all().order_by('-gtime')[:4]
    #新鲜蔬菜
    sc = TypeInfo.objects.all()[4]
    xxsc = sc.goodsinfo_set.all().order_by('-gtime')[:4]
    #速冻食品
    sp =TypeInfo.objects.all()[5]
    sdsp = sp.goodsinfo_set.all().order_by('-gtime')[:4]

    return render(request,'index.html',context={'goods':goods,'xxsg':xxsg,'hxsc':hxsc,'zrny':zrny,'qldp':qldp,'xxsc':xxsc,'sdsp':sdsp})
    #return render(request,'index.html',context={'goods':goods,'xxsg':xxsg})



def detail(request):
    return render(request,'detail.html')
