from django import forms
from apps.user import models


class RegisterModelForm(forms.ModelForm):
    repeatPassword = forms.CharField(label="确认密码")
    phone_code = forms.CharField(label="手机验证码")

    class Meta:
        model = models.UserAdminInfo
        fields = ['user_name', 'user_account', 'password', 'phone_number', 'email', 'repeatPassword', 'phone_code']


class LoginForm(forms.Form):
    user_account = forms.CharField(label="用户名", required=True)
    password = forms.CharField(label="密码", required=True)
    isadmin = forms.CharField(label="是否管理员", required=False)
