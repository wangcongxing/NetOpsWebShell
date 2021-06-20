from django.db import transaction
from django.shortcuts import render
from rest_framework.decorators import action
from rest_framework import viewsets, serializers, status
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import RetrieveAPIView
from rest_framework.pagination import PageNumberPagination
from app import models, modelFilters, modelSerializers, modelPermission
from utils import APIResponseResult
from utils.CustomViewBase import CustomViewBase
from django.contrib.auth.models import User, Group, Permission
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.hashers import make_password
from django.db.models import Q
from rest_framework.views import APIView
import os, uuid, time
from rest_framework_jwt.settings import api_settings
from django.contrib.auth.hashers import make_password
from django.http import JsonResponse, HttpResponse, HttpResponseRedirect
# 定时任务
import json
from datetime import datetime, timedelta
from django.db import transaction
from rest_framework import generics, mixins, views, viewsets
from django_filters import rest_framework as filters
import ast

# Create your views here.

# webSiteSet userInfo 只留下put方法
# 获取token时 同步新增userInfo
# init 新增默认网站设置数据webSiteSet
# 配置左侧菜单
# IntervalSchedule 数据存储异常的问题【seconds，5秒】

from django.core.cache import cache  # 引入缓存模块

ENV_PROFILE = os.getenv("ENV")
if ENV_PROFILE == "pro":
    from NetOpsWebShell import pro_settings as config
elif ENV_PROFILE == "test":
    from NetOpsWebShell import test_settings as config
else:
    from NetOpsWebShell import settings as config


# 默认数据初始化
class opsBaseInitDB(APIView):
    authentication_classes = ()
    permission_classes = ()

    def get(self, request, *args, **kwargs):

        return HttpResponse("<h1>数据库初始化成功</h1>")

from django.shortcuts import render, HttpResponse
from utils.tools import unique

import os


def index(request):
    return render(request, 'index.html')


def upload_ssh_key(request):
    if request.method == 'POST':
        pkey = request.FILES.get('pkey')
        ssh_key = pkey.read().decode('utf-8')

        while True:
            filename = unique()
            ssh_key_path = os.path.join(config.TMP_DIR, filename)
            if not os.path.isfile(ssh_key_path):
                with open(ssh_key_path, 'w') as f:
                    f.write(ssh_key)
                break
            else:
                continue

        return HttpResponse(filename)

