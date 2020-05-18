from django.core.paginator import PageNotAnInteger
from django.shortcuts import render
from django.views.generic import View

# Create your views here.
from pure_pagination import Paginator

from courses.models import Course


class CourseListView(View):
    def get(self, request):
        # 数据库中取出所有课程
        all_courses = Course.objects.all().order_by("-create_time")
        # 热门推荐
        hot_courses = Course.objects.all().order_by("-click_nums")[:3]
        # 学习人数和课程排序
        sort = request.GET.get('sort', "")
        if sort:
            if sort == "hot":
                all_courses = all_courses.order_by("-click_nums")
            elif sort == "students":
                all_courses = all_courses.order_by("-students")

        # 课程分页
        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1

        p = Paginator(all_courses, 9, request=request)

        courses = p.page(page)

        return render(request, "course-list.html", {
            "all_courses": courses,
            "sort": sort,
            "hot_courses": hot_courses
        })


class CourseDetailView(View):
    """
    课程详情页面
    """
    def get(self, request, course_id):
        course = Course.objects.get(id=int(course_id))
        # 增加课程点击数
        course.click_nums += 1
        course.save()
        return render(request, "course-detail.html", {
            "course": course
        })
