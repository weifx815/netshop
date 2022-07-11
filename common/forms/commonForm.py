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

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)  # 初始化父类方法
        for name, field in self.fields.items():
            field.widget.attrs = {'class': 'form-control',
                                  'placeholder': field.label,
                                  'title': field.label,
                                  'id': name}


class ROLEMenuModelForm(forms.ModelForm):

    class Meta:
        model = models.SysRoleMenu
        fields = ['role_id', 'menu_id']


class CodeTableManageForm(forms.ModelForm):
    class Meta:
        model = models.SysCodeTablesManage
        fields = ['code_table', 'code_table_name', 'valid_status']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)  # 初始化父类方法
        for name, field in self.fields.items():
            field.widget.attrs = {'class': 'form-control',
                                  'placeholder': field.label,
                                  'title': field.label,
                                  'id': name}


class CodeTableForm(forms.ModelForm):
    class Meta:
        model = models.SysCodeTables
        fields = ['code', 'name', 'code_table', 'valid_status']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)  # 初始化父类方法
        for name, field in self.fields.items():
            field.widget.attrs = {'class': 'form-control',
                                  'placeholder': field.label,
                                  'title': field.label,
                                  'id': name}
