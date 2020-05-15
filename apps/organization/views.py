# -*- coding: utf-8 -*-
from django.core.paginator import PageNotAnInteger
from django.shortcuts import render

# Create your views here.
from django.views.generic import View
from pure_pagination import Paginator

from organization.models import CourseOrg, CityDict


class OrgView(View):
    """
    课程机构列表功能
    """

    def get(self, request):
        # 课程机构
        all_orgs = CourseOrg.objects.all()
        # 热门机构排序
        hot_orgs = all_orgs.order_by("-click_nums")[:3]
        # 所有城市
        all_citys = CityDict.objects.all()
        # 城市筛选
        city_id = request.GET.get('city', "")
        if city_id:
            # 数据库查询通过城市字段进行筛选
            all_orgs = all_orgs.filter(city_id=int(city_id))
        # 类别筛选
        category = request.GET.get('ct', "")
        if category:
            # 数据库查询通过机构类别字段进行筛选
            all_orgs = all_orgs.filter(category=category)
        # 统计筛选结束后all_orgs的数量
        org_nums = all_orgs.count()
        # 学习人数和课程排序
        sort = request.GET.get('sort', "")
        if sort:
            if sort == "students":
                all_orgs = all_orgs.order_by("-students")
            elif sort == "courses":
                all_orgs = all_orgs.order_by("-course_nums")
        # 对课程机构进行分页
        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1

        p = Paginator(all_orgs, 5, request=request)

        orgs = p.page(page)

        return render(request, "org-list.html", {
            "all_orgs": orgs,
            "all_citys": all_citys,
            "org_nums": org_nums,
            "category": category,
            "city_id": city_id,
            "hot_orgs": hot_orgs,
            "sort": sort,
        })
