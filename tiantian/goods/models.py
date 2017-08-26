# -*- coding: utf-8 -*-
from django.db import models
from tinymce.models import  HTMLField
#添加 商品 类别
class TypeInfo(models.Model):
	title = models.CharField(max_length=30,verbose_name='商品类别')
	isDelete = models.BooleanField(default=False)  #逻辑删除
	def __str__(self):
		return self.title
# 商品表
class GoodsInfo(models.Model):
	gtype= models.ForeignKey(TypeInfo) #类
	gtitle = models.CharField(max_length=20,verbose_name='商品名称')      #标题
	gimage = models.ImageField(upload_to='goods',verbose_name='上传图片') #上传目录
	gprice = models.DecimalField(max_digits=5,decimal_places=2,verbose_name='价格')     #价格
	gunit = models.CharField(max_length=20,default='500g',verbose_name='单位')  #单位500g
	gtime = models.DateTimeField(verbose_name='上架时间') # 上架时间
	gclick = models.IntegerField(default=0,verbose_name='人气')  # 人气|点击 点击
	isDetele = models.BooleanField(default=False) #逻辑删除
	gdigest = models.CharField(max_length=100,verbose_name='商品摘要')  # 摘要
	ginfo = HTMLField(verbose_name='商品介绍')  #商品介绍 文本 编辑器
	gkucun = models.IntegerField(verbose_name='库存')  #库存
	gtj = models.BooleanField(default=False,verbose_name='新品推荐')  # 新品推荐
	def __str__(self):
		return self.gtitle

