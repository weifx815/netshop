from django.shortcuts import render, HttpResponse, redirect
from common import models
from django.http import JsonResponse
from common.forms import commonForm
import json
# Create your views here.


def MenuList(request):
    return render(request, "menuList.html", {"menu_list": get_Menu_List("ALL")})


def menuEdit(request, mid):
    obj = models.SysMenu.objects.filter(id=mid).first()
    if request.method == "GET":
        menu_list = get_Menu_List('1')
        form_type = "edit"
        return render(request, "menuEdit.html", locals())
    if request.method == "POST":
        menu_form = commonForm.MenuModelForm(data=request.POST, instance=obj)
        if menu_form.is_valid():
            menu_form.save()
            return JsonResponse({'status': True, 'url': '/common/menu/list/'})
        else:
            return render(request, "menuEdit.html", {"menu_form": menu_form, "menu_list": get_Menu_List('1')})


def get_Menu_List(menu_level):
    if menu_level == "ALL":
        menu_list = models.SysMenu.objects.all().order_by('-id')
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
    models.SysMenu.objects.filter(id=mid).first().delete()
    models.SysRoleMenu.objects.filter(menu_id=mid).delete()
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
    models.SysRole.objects.filter(id=rid).first().delete()
    models.SysUserRole.objects.filter(role_id=rid).delete()
    models.SysRoleMenu.objects.filter(role_id=rid).delete()
    return redirect("/common/role/list/")


def RoleMenu(request, rid):
    rid = rid
    role_list = models.SysRoleMenu.objects.filter(role_id=rid)
    role_ids = []
    for role in role_list:
        role_ids.append(str(role.menu_id))
    menu_ids = ','.join(role_ids)
    menu_list = get_Menu_List("ALL")
    json_menu = []
    for menu in menu_list:
        menus = dict()
        menus['id'] = menu.menu_code
        menus['pId'] = menu.menu_parent_code
        menus['name'] = menu.menu_name
        json_menu.append(menus)
    jsonarr = json.dumps(json_menu, ensure_ascii=False)
    return render(request, "roleMenu.html", locals())


def SaveRoleMenu(request):
    menu_ids = request.POST.get("menuIds").split(",")
    rid = request.POST.get("rid")
    if len(menu_ids) == 0:
        return JsonResponse({'status': False})
    models.SysRoleMenu.objects.filter(role_id=rid).delete()
    for mid in menu_ids:
        models.SysRoleMenu.objects.create(menu_id=int(mid), role_id=rid)
    return JsonResponse({'status': True})


def addUserRole(request, uid):
    if request.method == "GET":
        role_list = models.SysRole.objects.filter(role_status='Y')
        form_type = 'addRole'
        return render(request, "userRole.html", locals())
    if request.method == "POST":
        models.SysUserRole.objects.filter(user_id=uid).delete()
        roles = request.POST.getlist("role")
        for rid in roles:
            models.SysUserRole.objects.create(user_id=uid, role_id=rid)
        return JsonResponse({'status': True})


def CodeTableManageList(request):
    code_list = models.SysCodeTablesManage.objects.all()
    return render(request, "codetablemanagelist.html", locals())


def CodeTableManageAdd(request):
    if request.method == "GET":
        ctm = commonForm.CodeTableManageForm()
        form_type = 'add'
        return render(request, "codetablemanage.html", locals())
    if request.method == "POST":
        ctm = commonForm.CodeTableManageForm(data=request.POST)
        if ctm.is_valid():
            ctm.save()
            return JsonResponse({'status': True})
        else:
            return JsonResponse({'status': False, "errors": ctm.errors})


def CodeTableManageEdit(request, mid):
    obj = models.SysCodeTablesManage.objects.filter(id=mid).first()
    if request.method == "GET":
        ctm = commonForm.CodeTableManageForm(instance=obj)
        form_type = 'edit'
        return render(request, "codetablemanage.html", locals())
    if request.method == "POST":
        ctm = commonForm.CodeTableManageForm(data=request.POST, instance=obj)
        if ctm.is_valid():
            ctm.save()
            return JsonResponse({'status': True})
        else:
            return JsonResponse({'status': False, "errors": ctm.errors})


def CodeTableManageDelete(request, mid):
    obj = models.SysCodeTablesManage.objects.filter(id=mid).first()
    obj.delete()
    return redirect("/common/codetable/manage/list/")


def CodeTableList(request):
    code_list = models.SysCodeTables.objects.all()
    return render(request, "codetablelist.html", locals())


def CodeTableAdd(request):
    if request.method == "GET":
        ctm = commonForm.CodeTableForm()
        form_type = 'add'
        return render(request, "codetable.html", locals())
    if request.method == "POST":
        ctm = commonForm.CodeTableForm(data=request.POST)
        if ctm.is_valid():
            ctm.save()
            return JsonResponse({'status': True})
        else:
            return JsonResponse({'status': False, "errors": ctm.errors})


def CodeTableEdit(request, mid):
    obj = models.SysCodeTables.objects.filter(id=mid).first()
    if request.method == "GET":
        ctm = commonForm.CodeTableForm(instance=obj)
        form_type = 'edit'
        return render(request, "codetable.html", locals())
    if request.method == "POST":
        ctm = commonForm.CodeTableForm(data=request.POST, instance=obj)
        if ctm.is_valid():
            ctm.save()
            return JsonResponse({'status': True})
        else:
            return JsonResponse({'status': False, "errors": ctm.errors})


def CodeTableDelete(request, mid):
    obj = models.SysCodeTables.objects.filter(id=mid).first()
    obj.delete()
    return redirect("/common/codetable/list/")

