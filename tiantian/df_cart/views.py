from django.shortcuts import render,redirect
from django.http import  HttpResponse,JsonResponse
from df_user.models import  UserInfo
from goods.models import GoodsInfo
from .models import  CartInfo

def cart(request):
	uid = request.session['user_id']

	carts = CartInfo.objects.filter(user_id = uid)
	return render(request,'cart.html')

def add(request,gid,count):
	uid = request.session['user_id']

	gid = int(gid)
	count = int(count)
	carts = CartInfo.objects.filter(user_id=uid,goods_id=gid)
	if len(carts)>=1:
		cart = carts[0]
		cart.count = cart.count+count
	else:
		cart = CartInfo()
		cart.user_id = uid
		cart.goods_id = gid
		cart.count = count

	if request.is_ajax():
		count = CartInfo.objects.filter(user_id=request.session['user_id']).count()
		return JsonResponse({'count':count})
	else:
		return redirect('/cart/')
def delete(request,cart_id):
	try:
	# 拿到删除的商品的ID
		cart = CartInfo.objects.get(pk = int(cart_id))
		cart.delete()
		data={'ok':1}
	except Exception as e:
		data={'ok':0}
	return JsonResponse(data)

def addnum(request):
	cid = request.POST.get('id')
	num = request.POST.get('s')
	cart = CartInfo.objects.filter(id=int(cid)).update(count=int(num))
	return HttpResponse('ok')


def gwc(request):
	if request.method == 'POST':
		gid = request.POST.get('gid')
		gcount = request.POST.get('gcount')
		gcount= int(gcount)
		uid = request.session["user_id"]
		print(uid)
		carts = CartInfo.objects.filter(user_id=uid, goods_id=gid)

		if len(carts) >= 1:
			cart = carts[0]
			cart.count = cart.count + gcount
		else:
			cart = CartInfo()
			cart.user_id = uid
			cart.goods_id = gid
			cart.count = gcount

		cart.save()
		return HttpResponse('添加购物车成功')  #添加 信息重复数量+1

def showcar(request):
	uname = request.COOKIES["uname"]
	pp = UserInfo.objects.filter(uname=uname)[0]
	uid = pp.id
	ee = CartInfo.objects.filter(user_id = uid)
	lena = len(ee)
	for i in ee:
		c = i.count
		print(i.count)


	# list = CartInfo.objects.filter(user_id=uid)

	return render(request,'cart.html',{'list':ee,'leng':lena})


