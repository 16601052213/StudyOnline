# -*- coding: utf-8 -*-
__author__ = 'zhuhai'
__date__ = '2020/5/17 15:50'

from django.conf.urls import url, include

from courses.views import CourseListView, CourseDetailView, CourseInfoView, CommentsView, AddComentsView

urlpatterns = [
    # 课程列表页
    url(r'^list/$', CourseListView.as_view(), name="course_list"),
    # 课程详情页
    url(r'^detail/(?P<course_id>\d+)/$', CourseDetailView.as_view(), name="course_detail"),
    # 章节信息页
    url(r'^info/(?P<course_id>\d+)/$', CourseInfoView.as_view(), name="course_info"),
    # 课程评论
    url(r'^comment/(?P<course_id>\d+)/$', CommentsView.as_view(), name="course_comments"),
    # 添加课程评论
    url(r'^add_comment/$', AddComentsView.as_view(), name="add_comment"),

]
