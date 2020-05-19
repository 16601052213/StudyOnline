# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from datetime import datetime

from django.db import models
from organization.models import CourseOrg, Teacher


# Create your models here.


class Course(models.Model):
    course_org = models.ForeignKey(CourseOrg, verbose_name=u"课程机构", null=True, blank=True)
    name = models.CharField(max_length=50, verbose_name=u"课程名")
    desc = models.CharField(max_length=300, verbose_name=u"课程描述")
    detail = models.TextField(verbose_name=u"课程详情")
    teacher = models.ForeignKey(Teacher, verbose_name=u"讲师", null=True, blank=True)
    degree = models.CharField(choices=(("cj", "初级"), ("zj", "中级"), ("gj", "高级")), max_length=2, verbose_name=u"难度")
    learn_times = models.IntegerField(default=0, verbose_name=u"学习时长(分)")
    students = models.IntegerField(default=0, verbose_name=u"学习人数")
    fav_nums = models.IntegerField(default=0, verbose_name=u"收藏人数")
    category = models.CharField(max_length=20, verbose_name=u"课程类别", default="后端开发")
    image = models.ImageField(upload_to="courses/%Y/%m", verbose_name=u"封面图", max_length=100)
    click_nums = models.IntegerField(default=0, verbose_name=u"点击数")
    create_time = models.DateTimeField(default=datetime.now, verbose_name=u"添加时间")
    tag = models.CharField(default="", verbose_name=u"课程标签", max_length=10)
    youneed_know = models.CharField(max_length=300, verbose_name=u"课程描述", default="")
    teacher_tell = models.CharField(max_length=300, verbose_name=u"老师告诉你课程须知", default="")

    class Meta:
        verbose_name = u"课程"
        verbose_name_plural = verbose_name

    def get_zj_nums(self):
        # 获取课程章节数
        return self.lesson_set.all().count()

    def get_learn_users(self):
        # 取出前五个学习用户
        return self.usercourse_set.all()[:5]

    def get_course_lesson(self):
        # 取出章节数
        return self.lesson_set.all()

    def __str__(self):
        return self.name


class Lesson(models.Model):
    course = models.ForeignKey(Course, verbose_name=u"课程")
    learn_times = models.IntegerField(default=0, verbose_name=u"学习时长(分)")
    name = models.CharField(max_length=100, verbose_name=u"章节名")
    url = models.CharField(max_length=200, verbose_name=u"访问地址", default="")
    create_time = models.DateTimeField(default=datetime.now, verbose_name=u"添加时间")

    class Meta:
        verbose_name = u"章节"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name

    def get_lesson_video(self):
        return self.video_set.all()


class Video(models.Model):
    lesson = models.ForeignKey(Lesson, verbose_name=u"章节")
    name = models.CharField(max_length=100, verbose_name=u"视频名")
    learn_times = models.IntegerField(default=0, verbose_name=u"学习时长(分)")
    url = models.CharField(max_length=200, verbose_name=u"访问地址", default="")
    create_time = models.DateTimeField(default=datetime.now, verbose_name=u"添加时间")

    class Meta:
        verbose_name = u"视频"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class CourseResource(models.Model):
    course = models.ForeignKey(Course, verbose_name=u"课程")
    name = models.CharField(max_length=100, verbose_name=u"名称")
    download = models.FileField(upload_to="course/resource/%Y/%m", verbose_name=u"资源文件", max_length=100)
    create_time = models.DateTimeField(default=datetime.now, verbose_name=u"添加时间")

    class Meta:
        verbose_name = u"课程资源"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name
