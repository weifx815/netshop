from django import template
from common import models

register = template.Library()


@register.inclusion_tag("menuShow.html")
def get_menu_html(request):
    user_id = request.session["userinfo"].get("id")
    isadmin = request.session["userinfo"].get("isadmin")
    if isadmin == 'Y':
        menu_list_1 = models.SysMenu.objects.filter(menu_level='1', menu_status='Y').order_by('menu_code')
        menu_list_2 = models.SysMenu.objects.filter(menu_level='2', menu_status='Y').order_by('menu_code')
        return {"menu_list_1": menu_list_1, "menu_list_2": menu_list_2}
    role_ids = models.SysUserRole.objects.filter(user_id=user_id).values("role_id")
    menu_ids = models.SysRoleMenu.objects.filter(role_id__in=role_ids).values("menu_id")
    menu_list_1 = models.SysMenu.objects.filter(menu_level='1', menu_status='Y', menu_code__in=menu_ids).order_by('menu_code')
    menu_list_2 = models.SysMenu.objects.filter(menu_level='2', menu_status='Y', menu_code__in=menu_ids).order_by('menu_code')
    return {"menu_list_1": menu_list_1, "menu_list_2": menu_list_2}
