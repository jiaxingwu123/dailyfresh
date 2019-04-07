# -*- coding: utf-8 -*-
from django.db import models

# Create your models here.

class OrderInfo(models.Model):
    oid = models.CharField(max_length=20,primary_key=True)  # 订单编号
    user = models.ForeignKey('df_user.UserInfo')       # 哪里的人下的订单
    odate = models.DateTimeField(auto_now=True)         # 下单的时间
    oIsPay = models.IntegerField(default=0)         # 是否支付
    ototal = models.DecimalField(max_digits=6,decimal_places=2)   # 总金额
    oaddress = models.CharField(max_length=150,default='')   # 收件地址
    zhifu = models.IntegerField(default=0)      # 支付类型

class OrderDetailInfo(models.Model):
    goods=models.ForeignKey('df_goods.GoodsInfo')
    order=models.ForeignKey(OrderInfo)
    price=models.DecimalField(max_digits=5,decimal_places=2)
    count=models.IntegerField()