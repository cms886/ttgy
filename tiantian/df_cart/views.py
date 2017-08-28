from django.shortcuts import render
from django.http import  HttpResponse
from df_user.models import  UserInfo
from goods.models import GoodsInfo
from .models import  CartInfo


# Create your views here.
def gwc(request):
	if request.method == 'POST':
		gid = request.POST.get('gid')
		gcount = request.POST.get('gcount')
		uname = request.COOKIES["uname"]
		print(uname)
		pp = UserInfo.objects.filter(uname=uname)[0]
		uid = pp.id
		obj =CartInfo(goods = gid,user = uid ,count = gcount)
		obj.save()
		return HttpResponse('add ok')

def showcar(request):
	uname = request.COOKIES["uname"]
	pp = UserInfo.objects.filter(uname=uname)[0]
	uid = pp.id
	obj = CartInfo.objects.filter(user=uid)
	glist = []
	for i in obj:
		gid = i.goods
		t = i.count
		g = GoodsInfo.objects.filter(id=gid)[0]
		title = g.gtitle
		image = g.gimage
		unit = g.gunit
		price = g.gprice
		glist.append(title)
		glist.append(image)
		glist.append(unit)
		glist.append(price)
		glist.append(t)
	return render(request,'cart.html',{'list':glist,'t':t})


