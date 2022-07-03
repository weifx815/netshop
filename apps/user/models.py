from django.db import models
from db.base_model import BaseModel
from utils import options


class UserInfo(BaseModel):
    """用户信息表"""
    user_name = models.CharField(verbose_name="姓名", max_length=100)
    user_account = models.CharField(verbose_name="登录用户名", max_length=50, db_index=True)
    password = models.CharField(verbose_name="密码", max_length=10, default='1234@abcd')
    gender = models.CharField(verbose_name="性别", choices=options.gender_choose, default='0', max_length=1)
    email = models.EmailField(verbose_name="电子邮箱", max_length=50)
    phone_number = models.CharField(verbose_name="手机号码", max_length=12)
    birthday = models.DateField(verbose_name="出生日期", null=True, blank=True)
    age = models.SmallIntegerField(verbose_name="年龄", null=True, blank=True)
    identity_card = models.CharField(verbose_name="身份证号", max_length=18)
    origin = models.CharField(verbose_name="籍贯", max_length=50, null=True, blank=True)
    address = models.CharField(verbose_name="详细住址", max_length=200, null=True, blank=True)
    company = models.CharField(verbose_name="所在公司名称", max_length=100, null=True, blank=True)
    account = models.DecimalField(verbose_name="账户余额", max_digits=20, decimal_places=2, default=0)
    registered_date = models.DateTimeField(verbose_name="注册时间", auto_now_add=True)
    recent_date = models.DateTimeField(verbose_name="最近一次登录时间", auto_now=True)
    valid_status = models.CharField(verbose_name="有效状态(默认Y有效)", choices=options.valid_choose, default='Y', max_length=1)

    class Meta:
        # 定义表名
        db_table = 'user_info'
        verbose_name = '注册用户信息表'
        verbose_name_plural = verbose_name


class UserAdminInfo(BaseModel):
    """后台店铺用户信息表"""
    user_name = models.CharField(verbose_name="姓名", max_length=100)
    user_account = models.CharField(verbose_name="登录用户名", max_length=50, db_index=True)
    password = models.CharField(verbose_name="密码", max_length=10, default='root')
    province = models.CharField(verbose_name="所在省", max_length=100, null=True, blank=True)
    province_code = models.CharField(verbose_name='所在省代码', max_length=50, null=True, blank=True)
    city = models.CharField(verbose_name="所在市", max_length=100, null=True, blank=True)
    city_code = models.CharField(verbose_name="所在市代码", max_length=50, null=True, blank=True)
    phone_number = models.CharField(verbose_name="手机号码", max_length=12)
    identity_card = models.CharField(verbose_name="身份证号", max_length=18, null=True, blank=True)
    address = models.CharField(verbose_name="详细住址", max_length=200, null=True, blank=True)
    email = models.EmailField(verbose_name="电子邮箱", max_length=50, null=True, blank=True)
    company = models.CharField(verbose_name="公司名称", max_length=100, null=True, blank=True)
    sales = models.DecimalField(verbose_name="销售总额", max_digits=20, decimal_places=2, default=0)
    registered_date = models.DateTimeField(verbose_name="创建时间", auto_now_add=True)
    login_frequency = models.SmallIntegerField(verbose_name="登录次数", default=0)
    recent_date = models.DateTimeField(verbose_name="最近一次登录时间")
    valid_status = models.CharField(verbose_name="有效状态(默认Y有效)", choices=options.valid_choose, default='Y', max_length=1)

    class Meta:
        db_table = 'user_admin_info'
        verbose_name = '后台店铺用户信息表'
        verbose_name_plural = verbose_name


class SysAdminInfo(BaseModel):
    """系统后台管理员表信息"""
    user_name = models.CharField(verbose_name="姓名", max_length=100)
    user_account = models.CharField(verbose_name="登录用户名", max_length=50, db_index=True)
    password = models.CharField(verbose_name="密码", max_length=10, default='admin')
    phone_number = models.CharField(verbose_name="手机号码", max_length=12)
    recent_date = models.DateTimeField(verbose_name="最近一次登录时间", auto_now=True)

    class Meta:
        db_table = 'sys_admin_info'
        verbose_name = '系统后台管理员表信息'
        verbose_name_plural = verbose_name
