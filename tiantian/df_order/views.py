from django.shortcuts import render
from django.shortcuts import render,HttpResponse,redirect
from  df_cart.models import  CartInfo
from goods.models import GoodsInfo
from df_user.models import UserInfo
from .models import  OrderInfo,OrderDetailInfo
from datetime import  datetime
from django.db import transaction
# Create your views here.

#支付页
def place(request):
	#获取登录用户id
	#order = request.GET.getlist('cart_id')
	uid = request.session['user_id']
	# 显示地址
	uadress = UserInfo.objects.get(id = uid)
	carts = CartInfo.objects.filter(user_id=uid)
	a =  CartInfo.objects.filter(user_id=uid).count()
	# print(a)
	context = {'carts':carts,'count':a,'adress':uadress}
	return render(request,'place_order.html',context)

#支付提交页面
#@transaction.atomic()
def placeSubmit(request):
#创建订单对象
	#tran_id = transaction.savepoint()
	try:
		uid = request.session['user_id']
		order = OrderInfo()
		now = datetime.now()
		order.oid ='%s%d'%(now.strftime('%Y%m%d%H%M%S'),uid)
		order.user_id = uid
		order.odate = now
		order.oIsPay = request.POST['pay_style']
		order.ototal = request.POST['ototal']
		order.oaddress = request.POST['adress']
		order.save()
	#判断商品 库存
		#创建详单对象
		carts = CartInfo.objects.filter(user_id=uid)
		for e in carts:
			gwcid = int(e.id)
			detail = OrderDetailInfo()
			detail.order = order
			#查询购物车信息
			cart = CartInfo.objects.get(id=gwcid)
			#判断商品库存
			goods = cart.goods  #连接商品
			if goods.gkucun>=cart.count: # 如果库存大于购买数量
				goods.gkucun = cart.goods.gkucun-cart.count
				goods.save()
				detail.goods_id = goods.id
				detail.price = goods.gprice
				detail.count = cart.count
				detail.save()
				#删除 购物车
				cart.delete()
			else:#如果 库存 小于购买数量
				transaction.savepoint_rollback(tran_id)
				return redirect('/cart/showcar/')
		#transaction.savepoint_rollback(tran_id)
	except Exception as e:
		print('=====================%s'%e)
		#transaction.savepoint_rollback(tran_id)

	return redirect('/user/user_center_order/')


#创建详情对象
#修改商品库存
#删除购物车










