import faker
from django.shortcuts import render, HttpResponse
from faker import Faker
from apps.user import models
from utils.produce_test_date import GetSysAdminInfo
from django.forms import forms
# Create your views here.


def login(requset):
    print("登录")
    return render(requset, "login.html")


def register(requset):
    return render(requset, "register.html")


def fakedata(requset):
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

