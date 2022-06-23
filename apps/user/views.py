import faker
from django.shortcuts import render, HttpResponse
from faker import Faker
from apps.user import models
from utils.produce_test_date import GetSysAdminInfo
from django.http import JsonResponse
from apps.user.forms.registerModelForm import RegisterModelForm
from django.db.models import Q
# Create your views here.


def login(request):
    print("登录")
    return render(request, "login.html")


def register(request):
    if request.method == "GET":
        form = RegisterModelForm()
        return render(request, "register.html", {"form": form})
    if request.method == "POST":
        form = RegisterModelForm(data=request.POST)
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

