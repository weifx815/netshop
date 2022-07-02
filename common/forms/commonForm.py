from django import forms
from common import models


class MenuModelForm(forms.ModelForm):

    class Meta:
        model = models.SysMenu
        fields = ['menu_name', 'menu_code', 'menu_level', 'menu_parent_code', 'menu_url', 'menu_img', 'menu_status']


class RoleModelForm(forms.ModelForm):

    class Meta:
        model = models.SysRole
        fields = ['role_name', 'role_describe', 'role_status']

    def __int__(self, *args, **kwargs):
        print("333333333334343434434")
        super(RoleModelForm, self).__init__(*args, **kwargs)
        print(self.fields.items())
        for name, field in self.fields.items():
            print(name+"===="+field.label)
            field.widget.attrs.update({"class": "form-control", "placeholder": field.label})

