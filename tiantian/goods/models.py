from django.db import models
from tinymce.models import  HTMLField
#添加 商品 类别
class TypeInfo(models.Model):
	title = models.CharField(max_length=30)
	isDelete = models.BooleanField(default=False)  #逻辑删除
	def __str__(self):
		return self.title.encode('utf-8')
# 商品表
class GoodsInfo(models.Model):
	gtype= models.ForeignKey(TypeInfo) #类
	gtitle = models.CharField(max_length=20)      #标题
	gimage = models.ImageField(upload_to='goods') #上传目录
	gprice = models.DecimalField(max_digits=5,decimal_places=2)     #价格
	gunit = models.CharField(max_length=20,default='500g')  #单位500g
	gtime = models.DateTimeField() # 上架 时间
	gclick = models.IntegerField(default=0)  # 人气|点击 点击量
	isDetele = models.BooleanField(default=False) #逻辑删除
	gdigest = models.CharField(max_length=100)  # 摘要
	ginfo = HTMLField()  #商品介绍 文本 编辑器 
	gkucun = models.IntegerField()  #库存
	gtj = models.BooleanField(default=False)  # 新品推荐

	def __str__(self):
		return self.gtitle.encode('utf-8')

