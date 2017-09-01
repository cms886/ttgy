from django.shortcuts import render

from django.shortcuts import render
from  df_cart.models import  CartInfo
from goods.models import GoodsInfo
# Create your views here.

#支付页
def place(request):
	#获取登录用户id
	#order = request.GET.getlist('cart_id')
	uid = request.session['user_id']
	carts = CartInfo.objects.filter(user_id=uid)
	context = {'carts':carts}
	return render(request,'place_order.html',context)

