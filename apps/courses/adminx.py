# -*- coding: utf-8 -*-
__author__ = 'zhuhai'
__date__ = '2020/5/7 19:09'

import xadmin
from .models import Course, Lesson, Video, CourseResource, BannerCousrse


class LessonInline(object):
    model = Lesson
    extra = 0


class CourseAdmin(object):
    list_display = ['name', 'desc', 'detail', 'degree', 'learn_times', 'students', 'click_nums', 'create_time',
                    'get_zj_nums']
    search_fields = ['name', 'desc', 'detail', 'degree', 'learn_times', 'students', 'click_nums']
    list_filter = ['name', 'desc', 'detail', 'degree', 'learn_times', 'students', 'click_nums', 'create_time',
                   ]
    ordering = ['-click_nums']
    readonly_fields = ['click_nums']
    exclude = ['fav_nums']
    inlines = [LessonInline]
    list_editable = ['degree', 'desc']

    def queryset(self):
        qs = super(CourseAdmin, self).queryset()
        qs = qs.filter(is_banner=False)
        return qs

    def save_models(self):
        # 在保存课程的时候统计课程机构的课程数
        obj = self.new_obj
        obj.save()
        if obj.course_org is not None:
            course_org = obj.course_org
            course_org.course_nums = Course.objects.filter(course_org=course_org)
            course_org.save()


class BannerCousrseAdmin(object):
    list_display = ['name', 'desc', 'detail', 'degree', 'learn_times', 'students', 'click_nums', 'create_time']
    search_fields = ['name', 'desc', 'detail', 'degree', 'learn_times', 'students', 'click_nums']
    list_filter = ['name', 'desc', 'detail', 'degree', 'learn_times', 'students', 'click_nums', 'create_time']
    ordering = ['-click_nums']
    readonly_fields = ['click_nums']
    exclude = ['fav_nums']
    inlines = [LessonInline]

    def queryset(self):
        qs = super(BannerCousrseAdmin, self).queryset()
        qs = qs.filter(is_banner=True)
        return qs


class LessonAdmin(object):
    list_display = ['course', 'name', 'create_time']
    search_fields = ['course', 'name']
    list_filter = ['course', 'name', 'create_time']


class VideoAdmin(object):
    list_display = ['lesson', 'name', 'create_time']
    search_fields = ['lesson', 'name']
    list_filter = ['lesson', 'name', 'create_time']


class CourseResourceAdmin(object):
    list_display = ['course', 'name', 'download', 'create_time']
    search_fields = ['course', 'name', 'download']
    list_filter = ['course', 'name', 'download', 'create_time']


xadmin.site.register(Course, CourseAdmin)
xadmin.site.register(BannerCousrse, BannerCousrseAdmin)

xadmin.site.register(Lesson, LessonAdmin)
xadmin.site.register(Video, VideoAdmin)
xadmin.site.register(CourseResource, CourseResourceAdmin)
