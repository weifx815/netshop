from django.shortcuts import render, HttpResponse, redirect
from common import models
from django.http import JsonResponse
from common.forms import commonForm
# Create your views here.


def MenuList(request):
    user_id = request.session["userinfo"].get("id")
    return render(request, "menuList.html", {"menu_list": get_Menu_List("ALL"), "user_id": str(user_id)})


def menuEdit(request, mid):
    obj = models.SysMenu.objects.filter(id=mid).first()
    menu_list = get_Menu_List('1')
    form_type = "edit"
    return render(request, "menuEdit.html", locals())


def get_Menu_List(menu_level):
    if menu_level == "ALL":
        menu_list = models.SysMenu.objects.all().order_by('-update_time')
    else:
        menu_list = models.SysMenu.objects.filter(menu_level=menu_level, menu_status='Y').order_by('menu_code')
    return menu_list


def menuAdd(request):
    if request.method == "GET":
        menu_form = commonForm.MenuModelForm()
        form_type = "add"
        return render(request, "menuEdit.html", {"menu_form": menu_form, "menu_list": get_Menu_List('1'), "form_type": form_type})
    if request.method == "POST":
        menu_form = commonForm.MenuModelForm(data=request.POST)
        if menu_form.is_valid():
            menu_form.save()
            return JsonResponse({'status': True, 'url': '/common/menu/list/'})
        else:
            return render(request, "menuEdit.html", {"menu_form": menu_form, "menu_list": get_Menu_List('1')})


def menuView(request, mid):
    obj = models.SysMenu.objects.filter(id=mid).first()
    return render(request, "menuView.html", {"obj": obj})


def menuDelete(request, mid):
    obj = models.SysMenu.objects.filter(id=mid).first()
    obj.delete()
    return redirect("/common/menu/list/")


def RoleList(request):
    role_list = models.SysRole.objects.all()
    return render(request, "roleList.html", locals())


def RoleAdd(request):
    if request.method == "GET":
        role_from = commonForm.RoleModelForm()
        form_type = "add"
        return render(request, "roleEdit.html", locals())
    if request.method == "POST":
        role_from = commonForm.RoleModelForm(data=request.POST)
        if role_from.is_valid():
            role_from.save()
            return JsonResponse({'status': True})
        else:
            return JsonResponse({'status': False, "errors": role_from.errors})


def RoleEdit(request, rid):
    obj = models.SysRole.objects.filter(id=rid).first()
    if request.method == "GET":
        role_from = commonForm.RoleModelForm(instance=obj)
        form_type = "edit"
        return render(request, "roleEdit.html", locals())
    if request.method == "POST":
        role_from = commonForm.RoleModelForm(data=request.POST, instance=obj)
        if role_from.is_valid():
            role_from.save()
            return JsonResponse({'status': True})
        else:
            return JsonResponse({'status': False, "errors": role_from.errors})


def RoleDelete(request, rid):
    obj = models.SysRole.objects.filter(id=rid).first()
    obj.delete()
    return redirect("/common/role/list/")

