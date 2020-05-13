# -*- coding: utf-8 -*-
from django.shortcuts import render

# Create your views here.
from django.views.generic import View

from organization.models import CourseOrg, CityDict


class OrgView(View):
    """
    课程机构列表功能
    """

    def get(self, request):
        # 课程机构
        all_orgs = CourseOrg.objects.all()
        # 城市
        all_citys = CityDict.objects.all()

        return render(request, "org-list.html", {
            "all_orgs":all_orgs,
            "all_citys":all_citys
        })
