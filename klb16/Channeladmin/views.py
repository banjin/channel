# -*-coding:utf-8 -*-
from django.shortcuts import *
from django.contrib.auth.hashers import make_password, check_password
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
# from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse
from models import *


def Register(request):
    if request.method == "POST":
        username = request.REQUEST.get("username", '')
        password = request.REQUEST.get("password", '')
        repassword = request.REQUEST.get("repassword", '')
        email = request.REQUEST.get('email', '')
        if password != repassword:
            return render_to_response('channeladmin/regerr.html', {})
        else:
            User.objects.create(username=username, password=password, email=email)
            return render_to_response('channeladmin/regsuc.html', {})


def Login(request):
    if request.method == "POST":
        username = request.REQUEST.get("username", '')
        password = request.REQUEST.get("password", '')
        if User.objects.filter(username=username, password=password) or \
                User.objects.filter(username=username, password=password):
            return render_to_response('channeladmin/index.html',{})

    print u"登录失败"
    return render_to_response('channeladmin/login.html',{})


def Index(request):
    return render_to_response("channeladmin/index.html",{})


def Logout(request):
    logout(request)
    request.session["klb_username"] = ""
    return HttpResponseRedirect("/channeladmin/Login/")

