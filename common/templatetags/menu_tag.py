from django import template
from common import models


register = template.Library()


@register.inclusion_tag("menuShow.html")
def get_menu_html(user_id):
    print("用户id========================="+user_id)
    menu_list_1 = models.SysMenu.objects.filter(menu_level='1', menu_status='Y').order_by('menu_code')
    menu_list_2 = models.SysMenu.objects.filter(menu_level='2', menu_status='Y').order_by('menu_code')
    return {"menu_list_1": menu_list_1, "menu_list_2": menu_list_2}
