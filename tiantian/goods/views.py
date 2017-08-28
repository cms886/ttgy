# -*- coding: utf-8 -*-
from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from .models import TypeInfo,GoodsInfo
from django.core.paginator import Paginator,EmptyPage
def index(request):
    #商品类
    goods = TypeInfo.objects.all().order_by()[:6]  # 取出最新信息前6条
    #商品名称
    #post_list = GoodsInfo.objects.all().order_by('-gtime')[:4]   #取出最新信息前4条
    # 楼层
    p = TypeInfo.objects.all()[0]
    xxsg = p.goodsinfo_set.all().order_by('gtime')[:4]
    #海鲜水产
    type = TypeInfo.objects.all()[1]
    hxsc = type.goodsinfo_set.all().order_by('gtime')[:4]
    #猪肉 牛羊
    r = TypeInfo.objects.all()[2]
    zrny = r.goodsinfo_set.all().order_by('gtime')[:4]
    #禽类蛋品
    dan = TypeInfo.objects.all()[3]
    qldp = dan.goodsinfo_set.all().order_by('gtime')[:4]
    #新鲜蔬菜
    sc = TypeInfo.objects.all()[4]
    xxsc = sc.goodsinfo_set.all().order_by('gtime')[:4]
    #速冻食品
    sp =TypeInfo.objects.all()[5]
    sdsp = sp.goodsinfo_set.all().order_by('gtime')[:4]

    return render(request,'index.html',context={'goods':goods,'xxsg':xxsg,'hxsc':hxsc,'zrny':zrny,'qldp':qldp,'xxsc':xxsc,'sdsp':sdsp})


def detail(request,id):
    goodsinfo = get_object_or_404(GoodsInfo,id = id)
    return render(request,'detail.html',context={'goodsinfo':goodsinfo})


#全部list
def goodslist(request, pIndex):
    #新品推荐
    tj = GoodsInfo.objects.filter(gtj=True).order_by('-gtime')[:2]
    #分页显示
    list1 = GoodsInfo.objects.all()
    p = Paginator(list1,15)
    if pIndex == '':
        pIndex = '1'
    pIndex = int(pIndex)
    #取第几分页对象
    list2 = p.page(pIndex)
    plist = p.page_range
    return render(request, 'list.html', {'list': list2, 'plist': plist, 'pIndex': pIndex,'tj':tj})

def typelist(request,typeid):
    r = TypeInfo(id=typeid)
    jgj = r.goodsinfo_set.all()
    # paginator = Paginator(jgj, 15)  # Show 25 contacts per page
    # page = request.GET.get('page')
    # try:
    #     contacts = paginator.page(page)
    # except PageNotAnInteger:
    #     contacts = paginator.page(1)
    # except EmptyPage:
    #     contacts = paginator.page(paginator.num_pages)

    # 取第几分页对象
    return render(request, 'typelist.html', {'list': jgj})



