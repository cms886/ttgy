#coding=utf-8
from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect
from .models import *
from hashlib import sha1
from django.http import JsonResponse

#进入注册页面
def index(request):
    print(request,type(request))
    return render(request,'df_user/register.html')

#判断账号是否被注册
def register_exist(request):
    uname = request.GET.get('uname')
    print(request.GET)
    count = UserInfo.objects.filter(uname=uname).count()
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
    #request是
    uname = request.COOKIES.get('uname','')
    context = {'title':'用户登录','error_name':0,'error_pwd':0,'uname':uname}
    return render(request,'df_user/login.html',context)

#
def login_handle(request):
    post = request.POST
    uname = post.get('username')
    upwd = post.get('pwd')
    jizhu = post.get('jizhu',0)
    users = UserInfo.objects.filter(uname=uname)
    if len(users) == 1:
        s1 = sha1()
        s1.update(upwd.encode("gb2312"))
        if s1.hexdigest() == users[0].upwd:
            red = HttpResponseRedirect('/user/info/')
            if jizhu != 0:
                red.set_cookie('uname',uname)
            else:
                red.set_cookie('uname','',max_age=-1)

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

#
def info(request):
    user_mail = UserInfo.objects.get(id=request.session['user_id']).umail
    context = {
        # 'title':'用户中心',
        'user_mail':user_mail,
        'user_name':request.session['user_name']}
    return render(request,'df_user/user_center_info.html',context)

#
def user_center_info(request):
    user_mail = UserInfo.objects.get(id=request.session['user_id']).umail
    context = {
        # 'title':'用户中心',
        'user_mail': user_mail,
        'user_name': request.session['user_name']}
    return render(request,'df_user/user_center_info.html',context)

#
def user_center_order(request):
    return render(request,'df_user/user_center_order.html')

#
def user_center_site(request):
    user = UserInfo.objects.get(id=request.session['user_id'])
    return render(request,'df_user/user_center_site.html',{'user':user})

#
def user_center_site_add(request):
    post = request.POST
    name = post.get('name')
    adress = post.get('adress')
    postcode = post.get('postcode')
    phone = post.get('phone')

    user = UserInfo.objects.get(id=request.session['user_id'])
    user.uname = name
    user.uadress = adress
    user.upostcode = postcode
    user.uphone = phone
    user.save()

    return render(request,'df_user/user_center_site.html',{'user':user})


