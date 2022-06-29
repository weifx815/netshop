from django.shortcuts import render, HttpResponse, redirect
from common import models
from django.http import JsonResponse
from common.forms import menuForm
# Create your views here.


def userMenu(request):
    return render(request, "sysMenu.html", {"menu_list": get_Menu_List("ALL")})


def userRose(request):
    role_list = models.SysRole.objects.all()
    return render(request, "sysRole.html", locals())


def menuEdit(request):
    get_Menu_List('1')
    return render(request, "menuEdit.html", locals())


def get_Menu_List(menu_level):
    if menu_level == "ALL":
        menu_list = models.SysMenu.objects.all().order_by('menu_code')
    else:
        menu_list = models.SysMenu.objects.filter(menu_level=menu_level, menu_status='Y').order_by('menu_code')
    return menu_list


def menuSave(request):
    if request.method == "GET":
        menu_form = menuForm.MenuModelForm()
        return render(request, "menuEdit.html", {"menu_form": menu_form, "menu_list": get_Menu_List('1')})
    if request.method == "POST":
        menu_form = menuForm.MenuModelForm(data=request.POST)
        if menu_form.is_valid():
            menu_form.save()
            return JsonResponse({'status': True, 'url': '/common/menu/'})
        else:
            return render(request, "menuEdit.html", {"menu_form": menu_form, "menu_list": get_Menu_List('1')})
