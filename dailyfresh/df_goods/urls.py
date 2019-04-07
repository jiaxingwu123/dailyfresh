#!/usr/bin/python
# -*- coding: utf-8 -*-
from django.conf.urls import url
from . import views


urlpatterns=[
    url(r'^$',views.index),
    url(r'^list(\d+)_(\d+)_(\d+)/$',views.goodlist),
    url(r'^(\d+)/$', views.detail),
]