from django.db import models

#订单主表  
class OrderInfo(models.Model):
    #订单编号
    oid = models.CharField(max_length=20,primary_key=True)
    #用户信息 
    user = models.ForeignKey('df_user.UserInfo')
    #订单 日期
    odate = models.DateTimeField(auto_now=True)
    #是否支付  
    oIsPay = models.BooleanField(default = False)#默认没有支付
    #商品总金额
    ototal = models.DecimalField(max_digits=6,decimal_places=2)#（小数2位）
    #订单地址
    oaddress = models.CharField(max_length=100)
    
#订单详表
class OrderDetailInfo(models.Model):
    #商品
    goods = models.ForeignKey('goods.GoodsInfo')
    #属于那个订单
    order = models.ForeignKey(OrderInfo)
    #商品价格
    price = models.DecimalField(max_digits=5,decimal_places=2)
    #数量
    count = models.IntegerField()

