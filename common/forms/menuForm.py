from django import forms
from common import models


class MenuModelForm(forms.ModelForm):

    class Meta:
        model = models.SysMenu
        fields = ['menu_name', 'menu_code', 'menu_level', 'menu_parent_code', 'menu_url', 'menu_img', 'menu_status']

