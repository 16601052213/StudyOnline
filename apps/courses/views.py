from django.core.paginator import PageNotAnInteger
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import View

# Create your views here.
from pure_pagination import Paginator

from courses.models import Course, CourseResource
from operation.models import UserFavorite, CourseComments


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

        p = Paginator(all_courses, 3, request=request)

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

        has_fav_course = False
        has_fav_org = False

        if request.user.is_authenticated():
            if UserFavorite.objects.filter(user=request.user, fav_id=course.id, fav_type=1):
                has_fav_course = True
            if UserFavorite.objects.filter(user=request.user, fav_id=course.course_org.id, fav_type=2):
                has_fav_org = True
        tag = course.tag
        if tag:
            relate_courses = Course.objects.filter(tag=tag)[:1]
        else:
            relate_courses = []
        return render(request, "course-detail.html", {
            "course": course,
            "relate_courses": relate_courses,
            "has_fav_course": has_fav_course,
            "has_fav_org": has_fav_org,
        })


class CourseInfoView(View):
    """
    课程章节信息
    """

    def get(self, request, course_id):
        course = Course.objects.get(id=int(course_id))
        all_resources = CourseResource.objects.filter(course=course)
        return render(request, "course-video.html", {
            "course": course,
            "course_resources": all_resources,
        })


class CommentsView(View):
    """
    课程评论功能
    """

    def get(self, request, course_id):
        course = Course.objects.get(id=int(course_id))
        all_resources = CourseResource.objects.filter(course=course)
        all_comments = CourseComments.objects.all()
        return render(request, "course-comment.html", {
            "course": course,
            "course_resources": all_resources,
            "all_comments": all_comments
        })


class AddComentsView(View):
    """
    用户添加课程评论
    """

    def post(self, request):
        if not request.user.is_authenticated():
            # 判断用户登录状态
            return HttpResponse('{"status":"fail", "msg":"用户未登录"}',
                                content_type='application/json')
        course_id = int(request.POST.get("course_id", 0))
        comments = request.POST.get("comments", "")
        if course_id > 0 and comments:
            course_comments = CourseComments()
            course = Course.objects.get(id=int(course_id))
            course_comments.course = course
            course_comments.comments = comments
            course_comments.user = request.user
            course_comments.save()
            return HttpResponse('{"status":"success", "msg":"评论成功"}',
                                content_type='application/json')
        else:
            return HttpResponse('{"status":"fail", "msg":"评论失败"}',
                                content_type='application/json')
