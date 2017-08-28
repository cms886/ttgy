from django.shortcuts import render
from django.http import  HttpResponse
from df_user.models import  UserInfo
from .models import  CartInfo


# Create your views here.
def gwc(request):
	if request.method == 'POST':
		gid = request.POST.get('gid')
		gcount = request.POST.get('gcount')
		uname = request.COOKIES["uname"]
		pp = UserInfo.objects.filter(uname=uname)[0]
		uid = pp.id
		obj =CartInfo(goods = gid,user = uid ,count = gcount)
		obj.save()
		return HttpResponse('ok')

