#coding=utf-8
from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect
from .models import *
from hashlib import sha1
from django.http import JsonResponse

def index(request):
    return render(request,'df_user/register.html')


def register_handle(request):
    uname = request.POST['user_name']
    upwd = request.POST['pwd']
    upwd2 = request.POST['cpwd']
    umail = request.POST['email']

    if upwd != upwd2:
        return redirect('/user/register/')

    s1 = sha1()
    s1.update(upwd.encode("gb2312"))
    upwd3 = s1.hexdigest()

    user = UserInfo()
    user.uname = uname
    user.upwd = upwd3
    user.umail = umail
    user.save()
    # return render(request,'df_user/login.html')
    return redirect('/user/login/')

def register_exist(request):
    print(request)
    uname = request.GET.get('uname')
    print(request.GET)
    count = UserInfo.objects.filter(uname=uname).count()
    return JsonResponse({'count':count})

def login(request):
    uname = request.COOKIES.get('uname','')
    context = {'title':'用户登录','error_name':0,'error_pwd':0,'uname':uname}
    return render(request,'df_user/login.html',context)

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
            # print('1111111111111111111111')
            red = HttpResponseRedirect('/user/info/')
            if jizhu != 0:
                red.set_cookie('uname',uname)
                print(22222222222222222222222)
            else:
                red.set_cookie('uname','',max_age=-1)
                print(33333333333333333333333333333)

            request.session['user_id'] = users[0].id
            request.session['user_name'] = uname
            return red

        else:
            context = {'title': '用户登录', 'error_name': 0, 'error_pwd': 1}
            return render(request, 'df_user/login.html', context)

    else:
        context = {'title':'用户登录','error_name':1,'error_pwd':0}
        return render(request,'df_user/login.html',context)

def info(request):
    user_mail = UserInfo.objects.get(id=request.session['user_id']).umail
    context = {
        # 'title':'用户中心',
        'user_mail':request.session['user_name']}
    return render(request,'df_user/user_center_info.html')