# -*-coding:utf-8 -*-
from django.shortcuts import *
from django.contrib.auth.hashers import make_password, check_password
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from models import *


def Login(request):
    if request.method == "POST":
        username = request.REQUEST.get("username", '')
        password = request.REQUEST.get("password", '')
        print username
        print password
        if user.objects.filter(username=username, password=password):
            print "登陆成功"
            return render_to_response('channeladmin/index.html',{})

    print u"登录失败"
    return render_to_response('channeladmin/login.html',{})


def Index(request):
    return render_to_response("channeladmin/index.html",{})

