# -*- coding: utf-8 -*-
__author__ = 'zhuhai'
__date__ = '2020/5/23 11:34'

from django.conf.urls import url, include

from users.views import UserInfoView

urlpatterns = [
    # 用户信息
    url(r'^info/$', UserInfoView.as_view(), name="user_info")
]