# -*- coding: utf-8 -*-
__author__ = 'zhuhai'
__date__ = '2020/5/7 20:32'

import xadmin
from operation.models import UserAsk, CourseComments, UserFavorite, UserMessage, UserCourse


class UserAskAdmin(object):
    list_display = ['name', 'mobile', 'course_name', 'create_time']
    search_fields = ['name', 'mobile', 'course_name']
    list_filter = ['name', 'mobile', 'course_name', 'create_time']


class CourseCommentsAdmin(object):
    list_display = ['user', 'course', 'comments', 'create_time']
    search_fields = ['user', 'course', 'comments']
    list_filter = ['user', 'course', 'comments', 'create_time']


class UserFavoriteAdmin(object):
    list_display = ['user', 'fav_id', 'fav_type', 'create_time']
    search_fields = ['user', 'fav_id', 'fav_type']
    list_filter = ['user', 'fav_id', 'fav_type', 'create_time']


class UserMessageAdmin(object):
    list_display = ['user', 'message', 'has_read', 'create_time']
    search_fields = ['user', 'message', 'has_read']
    list_filter = ['user', 'message', 'has_read', 'create_time']


class UserCourseAdmin(object):
    list_display = ['user', 'course', 'create_time']
    search_fields = ['user', 'course']
    list_filter = ['user', 'course', 'create_time']


xadmin.site.register(UserAsk, UserAskAdmin)
xadmin.site.register(CourseComments, CourseCommentsAdmin)
xadmin.site.register(UserFavorite, UserFavoriteAdmin)
xadmin.site.register(UserMessage, UserMessageAdmin)
xadmin.site.register(UserCourse, UserCourseAdmin)
