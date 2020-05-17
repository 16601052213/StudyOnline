# -*- coding: utf-8 -*-
__author__ = 'zhuhai'
__date__ = '2020/5/17 15:50'

from django.conf.urls import url, include

from courses.views import CourseListView

urlpatterns = [
    # 课程列表页
    url(r'^list/$', CourseListView.as_view(), name="course_list"),
]
