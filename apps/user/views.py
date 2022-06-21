import faker
from django.shortcuts import render, HttpResponse
from faker import Faker
from apps.user import models
from utils.produce_test_date import GetSysAdminInfo
from django import forms
# Create your views here.


def login(requset):
    print("登录")
    return render(requset, "login.html")


def register(requset):
    if requset.method == "GET":
        form = RegisterModelForm()
    return render(requset, "register.html", {"form": form})
    if requset.method == "POST":
        form = RegisterModelForm(data=requset.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("Y", mimetype='application/javascript')
        else:
            return render(requset, "register.html", {"form": form})


class RegisterModelForm(forms.ModelForm):
    class Meta:
        model = models.UserAdminInfo
        fields = ['user_name', 'user_account', 'password', 'phone_number', 'email']


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

