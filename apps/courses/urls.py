# -*- coding: utf-8 -*-
__author__ = 'zhuhai'
__date__ = '2020/5/17 15:50'

from django.conf.urls import url, include

from courses.views import CourseListView, CourseDetailView

urlpatterns = [
    # 课程列表页
    url(r'^list/$', CourseListView.as_view(), name="course_list"),
    # 课程详情页
    url(r'^detail/(?P<course_id>\d+)/$', CourseDetailView.as_view(), name="course_detail"),

]
