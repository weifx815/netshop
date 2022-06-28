from django.shortcuts import render, HttpResponse, redirect
from common import models
from django.http import JsonResponse
from common.forms import menuForm
# Create your views here.


def userMenu(request):
    menu_list = models.SysMenu.objects.all().order_by('menu_code')
    return render(request, "sysMenu.html", {"menu_list": menu_list})


def userRose(request):
    role_list = models.SysRole.objects.all()
    return render(request, "sysRole.html", {"role_list": role_list})


def menuEdit(request):
    print("进来了=================================")
    qmenulsit = models.SysMenu.objects.filter(menu_level='1').order_by('menu_code')
    return render(request, "menuEdit.html", {"qmenulsit": qmenulsit})


def menuSave(request):
    if request.method == "GET":
        menu_form = menuForm.MenuModelForm()
        qmenulsit = models.SysMenu.objects.filter(menu_level='1')
        return render(request, "menuEdit.html", {"qmenulsit": qmenulsit, "menu_form": menu_form})
    if request.method == "POST":
        menu_form = menuForm.MenuModelForm(data=request.POST)
        if menu_form.is_valid():
            menu_form.save()
            return JsonResponse({'status': True, 'url': '/common/menu/'})
        else:
            qmenulsit = models.SysMenu.objects.filter(menu_level='1')
            return render(request, "menuEdit.html", {"qmenulsit": qmenulsit, "menu_form": menu_form})
