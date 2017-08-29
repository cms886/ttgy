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
		pp = UserInfo.objects.filter(uname=uname)[0]
		uid = pp.id
		print(uid,gid,gcount)
		#多对多
		u = UserInfo.objects.get(id=uid)
		g = GoodsInfo.objects.get(id=gid)
		s = CartInfo(goods = g,user = u,count=gcount).save()
		return HttpResponse('添加购物车成功')  #添加 信息重复数量+1

def showcar(request):
	# uname = request.COOKIES["uname"]
	# pp = UserInfo.objects.filter(uname=uname)[0]
	# uid = pp.id
	# obj = CartInfo.objects.filter(user=uid)
	# glist = []
	# for i in obj:
	# 	gid = i.goods
	# 	t = i.count
	# 	g = GoodsInfo.objects.filter(id=gid)[0]
	# 	title = g.gtitle
	# 	image = g.gimage
	# 	unit = g.gunit
	# 	price = g.gprice
	# 	glist.append(title)
	# 	glist.append(image)
	# 	glist.append(unit)
	# 	glist.append(price)
	# 	glist.append(t)


	uname = request.COOKIES["uname"]
	pp = UserInfo.objects.filter(uname=uname)[0]
	uid = pp.id
	list = CartInfo.objects.filter(user_id=uid)
	return render(request,'cart.html',{'list':list})


