# -*- coding: utf-8 -*-
from django.contrib import admin

from .models import TypeInfo,GoodsInfo

class TypeInfoAdmin(admin.ModelAdmin):
	list_display = ['id','title']

class GoodsInfoAdmin(admin.ModelAdmin):
	list_per_page = 15
	list_display = ['id', 'gtitle','gdigest','gprice','gkucun','gunit','gtime','gclick','isDetele','ginfo','gtj']
#把 新增加的 TypeInfoAdmin 也注册进来
admin.site.register(TypeInfo,TypeInfoAdmin)
admin.site.register(GoodsInfo,GoodsInfoAdmin)


# Register your models here.
