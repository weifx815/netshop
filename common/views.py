from django.shortcuts import render
from common import models
# Create your views here.


def userMenu(request):
    menu_list = models.SysMenu.objects.all()
    return render(request, "sysMenu.html", {"menu_list": menu_list})


def userRose(request):
    role_list = models.SysRole.objects.all()
    return render(request, "sysRole.html", {"role_list": role_list})


def menuEdit(request):
    print("进来了=================================")
    return render(request, "menuEdit.html")
