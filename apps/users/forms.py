# -*- coding: utf-8 -*-
__author__ = 'zhuhai'
__date__ = '2020/5/9 16:36'

from django import forms


class LoginForm(forms.Form):
    username = forms.CharField(required=True)
    password = forms.CharField(required=True, min_length=5)
