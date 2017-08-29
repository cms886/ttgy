from django.db import models

class CartInfo(models.Model):
    goods = models.ForeignKey('goods.GoodsInfo')  #这是 多对多 一个用户对应 多个商品
    user = models.ForeignKey('df_user.UserInfo') #  用户表
    count = models.IntegerField()

# Create your models here.
