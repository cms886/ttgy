#coding=utf-8
from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect
from .models import *
from hashlib import sha1
from django.http import JsonResponse
import django
from goods.models import GoodsInfo

#进入注册页面
def index(request):
    # print(request,type(request))
    print(isinstance(request,django.core.handlers.wsgi.WSGIRequest))
    return render(request,'df_user/register.html')

#判断账号是否被注册
def register_exist(request):
    uname = request.GET.get('uname')
    # print(request,request.GET,666666666666666666666666666666666666666)
    count = UserInfo.objects.filter(uname=uname).count()
    print(count)
    return JsonResponse({'count':count})

#如果账号没有被注册,则开始处理用户注册信息,提交后进入登录界面
def register_handle(request):
    uname = request.POST['user_name']
    upwd = request.POST['pwd']
    upwd2 = request.POST['cpwd']
    umail = request.POST['email']
    #判断两次输入的密码是否一致,不一致则进入注册页面
    if upwd != upwd2:
        return redirect('/user/register/')
    #对提交的密码加密,upwd3是加密后的密码
    s1 = sha1()
    s1.update(upwd.encode("gb2312"))
    upwd3 = s1.hexdigest()
    #创建UserInfo的实例化对象user,每一个用户的注册过程本质上讲都是一次实例化对象的过程
    user = UserInfo()
    user.uname = uname
    user.upwd = upwd3
    user.umail = umail
    user.save()
    return redirect('/user/login/')

#进入登录界面
def login(request):
    #request是WSGIRequest类的一个对象,COOKIES是WSGIRequest的一个方法,get是什么?
    #如果uname被存入cookie，则这里直接使用第一个参数uname,如果没有则为第二个参数
    #context参数'error_name','error_pwd'可以不填
    uname = request.COOKIES.get('uname','')
    print()
    context = {'title':'用户登录','error_name':0,'error_pwd':0,'uname':uname}
    return render(request,'df_user/login.html',context)

#填完数据进行处理,正常情况下，进入用户中心页面
def login_handle(request):
    post = request.POST
    uname = post.get('username')
    upwd = post.get('pwd')
    jizhu = post.get('jizhu',0)
    users = UserInfo.objects.filter(uname=uname)
    #判断数据库是否有当前用户名,没有则进入else直接输出“用户名错误”
    if len(users) == 1:
        s1 = sha1()
        s1.update(upwd.encode("gb2312"))
        #用户名正确的情况下，判断密码是否正确，不正确则进入else，输出“用户名错误”
        #正确且选择了“记住”,则用户名存入cookie,
        if s1.hexdigest() == users[0].upwd:
            red = HttpResponseRedirect('/user/info/')
            if jizhu != 0:
                # 因为HttpResponseRedirect继承于HttpResponse，所以set_cookie可以被调用
                red.set_cookie('uname',uname)
            else:
                red.set_cookie('uname','',max_age=-1)
            #将id存入数据库中的session表
            request.session['user_id'] = users[0].id
            print(request.session['user_id'])
            request.session['user_name'] = uname
            print(request.session['user_name'])
            return red

        else:
            context = {'title': '用户登录', 'error_name': 0, 'error_pwd': 1}
            return render(request, 'df_user/login.html', context)

    else:
        context = {'title':'用户登录','error_name':1,'error_pwd':0}
        return render(request,'df_user/login.html',context)

#进入用户中心界面,session将携带参数，进入用户中心
def info(request):
    user_mail = UserInfo.objects.get(id=request.session['user_id']).umail
    goods_ids = request.COOKIES.get('goods_ids','')
    goods_ids1 = goods_ids.split(',')
    goods_list = []
    if goods_ids1 != ['']:
        print(goods_ids1)
        for goods_id in goods_ids1:
            print(goods_id,type(goods_id))
            goods_list.append(GoodsInfo.objects.get(id=int(goods_id)))

    context = {
        # 'title':'用户中心',
        'user_mail':user_mail,
        'user_name':request.session['user_name'],
        'goods_list':goods_list
    }
    return render(request,'df_user/user_center_info.html',context)

#点击个人信息
def user_center_info(request):
    user_mail = UserInfo.objects.get(id=request.session['user_id']).umail
    goods_ids = request.COOKIES.get('goods_ids', '')
    goods_ids1 = goods_ids.split(',')
    goods_list = []
    if goods_ids1 != ['']:
        for goods_id in goods_ids1:
            print(goods_id, type(goods_id))
            goods_list.append(GoodsInfo.objects.get(id=int(goods_id)))
    context = {
        # 'title':'用户中心',
        'user_mail': user_mail,
        'user_name': request.session['user_name'],
        'goods_list': goods_list
    }
    return render(request,'df_user/user_center_info.html',context)

#点击全部订单
def user_center_order(request):
    return render(request,'df_user/user_center_order.html')

#点击送货地址
def user_center_site(request):
    # 通过session获取一个对象（此对象为一个人的信息）,默认会显示用户为收件人
    user = UserInfo.objects.get(id=request.session['user_id'])
    return render(request,'df_user/user_center_site.html',{'user':user})

#添加收货人信息，可以改变默认收件人
def user_center_site_add(request):
    post = request.POST
    name = post.get('name')
    adress = post.get('adress')
    postcode = post.get('postcode')
    phone = post.get('phone')
    # 将填的收件人信息存入数据库,
    user = UserInfo.objects.get(id=request.session['user_id'])
    user.uname = name
    user.uadress = adress
    user.upostcode = postcode
    user.uphone = phone
    user.save()
    return render(request,'df_user/user_center_site.html',{'user':user})
