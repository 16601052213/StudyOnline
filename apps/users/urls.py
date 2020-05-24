# -*- coding: utf-8 -*-
__author__ = 'zhuhai'
__date__ = '2020/5/23 11:34'

from django.conf.urls import url, include

from users.views import UserInfoView, UploadImageView, ModifyPersionPwdView, SendEmailCodeView, UpdateEmailView

urlpatterns = [
    # 用户信息
    url(r'^info/$', UserInfoView.as_view(), name="user_info"),
    # 用户头像上传
    url(r'^image/upload/$', UploadImageView.as_view(), name="image_upload"),
    # 用户个人中心修改密码
    url(r'^update/pwd/$', ModifyPersionPwdView.as_view(), name="update_pwd"),
    # 发送邮箱验证码
    url(r'^sendemail_code/$', SendEmailCodeView.as_view(), name="sendemail_code"),
    # 修改邮箱
    url(r'^update_email/$', UpdateEmailView.as_view(), name="update_email"),

]