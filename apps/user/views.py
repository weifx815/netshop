import faker
from django.shortcuts import render, HttpResponse, redirect
from faker import Faker
from apps.user import models
from utils.produce_test_date import GetSysAdminInfo
from django.http import JsonResponse
from apps.user.forms import userModelForm
from django.db.models import Q
from django.core import serializers
# Create your views here.


def login(request):
    if request.method == "GET":
        form = userModelForm.LoginForm()
        return render(request, "login.html", {'form': form})
    if request.method == "POST":
        form = userModelForm.LoginForm(data=request.POST)
        if form.is_valid():
            account = request.POST.get("user_account")
            password = request.POST.get("password")
            isadmin = request.POST.get("isadmin")
            if isadmin == 'Y':
                obj = models.SysAdminInfo.objects.filter(Q(user_account=account) | Q(phone_number=account)).filter(password=password).first()
            else:
                obj = models.UserAdminInfo.objects.filter(Q(user_account=account) | Q(phone_number=account) | Q(email=account)).filter(password=password).first()
            if not obj:
                form.add_error("password", "用户名或密码错误")
                return render(request, "login.html", {'form': form})
            request.session["userinfo"] = {"id": obj.id, "user_name": obj.user_name}
            return redirect("/index/")
        return render(request, "login.html", {'form': form})


def index(request):
    return render(request, "index.html")


def menu(request):
    print("已经进入menu.html")
    return render(request, "base.html")


def register(request):
    if request.method == "GET":
        form = userModelForm.RegisterModelForm()
        return render(request, "register.html", {"form": form})
    if request.method == "POST":
        form = userModelForm.RegisterModelForm(data=request.POST)
        form.save()
        return JsonResponse({'status': True, 'url': '/login/'})
    return JsonResponse({'status': False, 'error': "提交错误"})


def ifRegister(request):
    flag = "N"
    code = request.GET.get("code")
    obj = models.UserAdminInfo.objects.filter(Q(user_account=code) | Q(phone_number=code) | Q(email=code)).first()
    if obj:
        flag = "Y"
    return HttpResponse(flag)


def getPhoneCode(request):
    fake = Faker("zh-CN")
    code = request.GET.get("code")
    code = fake.random_number(digits=6)
    print("手机验证码："+str(code))
    return HttpResponse(code)


def fakedata(request):
    fake = Faker("zh-CN")
    GetSysAdminInfo.user_name = fake.name()
    GetSysAdminInfo.user_account = fake.email()
    GetSysAdminInfo.password = fake.password(special_chars=False)
    GetSysAdminInfo.phone_number = fake.phone_number()
    GetSysAdminInfo.recent_date = fake.date_this_month()
    info = GetSysAdminInfo
    models.SysAdminInfo.objects.create(user_name=info.user_name, password=info.password,
                                       user_account=info.user_account, phone_number=info.phone_number,
                                       recent_date=info.recent_date)
    return HttpResponse(info.user_name+"可以注册了")

