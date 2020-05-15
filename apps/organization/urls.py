# -*- coding: utf-8 -*-
__author__ = 'zhuhai'
__date__ = '2020/5/15 22:37'

from django.conf.urls import url, include

from organization.views import OrgView, AddUserAskView

urlpatterns = [
    # 课程机构列表页
    url(r'^list/$', OrgView.as_view(), name="org_list"),
    url(r'^add_ask/$',AddUserAskView.as_view(), name="add_ask"),

]

