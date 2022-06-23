from django import forms
from apps.user import models


class RegisterModelForm(forms.ModelForm):
    repeatPassword = forms.CharField(label="确认密码")
    phone_code = forms.CharField(label="手机验证码")

    class Meta:
        model = models.UserAdminInfo
        fields = ['user_name', 'user_account', 'password', 'phone_number', 'email', 'repeatPassword', 'phone_code']
