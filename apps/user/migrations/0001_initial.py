# Generated by Django 3.2.13 on 2022-06-19 10:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SysAdminInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('is_delete', models.CharField(choices=[('0', '正常'), ('1', '已删除')], default='0', max_length=1, verbose_name='删除标记(默认0未删除)')),
                ('data_exchange', models.CharField(default='0', max_length=1, verbose_name='数据交换位')),
                ('user_name', models.CharField(max_length=100, verbose_name='姓名')),
                ('user_account', models.CharField(max_length=50, verbose_name='登录用户名')),
                ('password', models.CharField(default='admin', max_length=10, verbose_name='密码')),
                ('phone_number', models.CharField(max_length=12, verbose_name='手机号码')),
                ('recent_date', models.DateTimeField(auto_now=True, verbose_name='最近一次登录时间')),
            ],
            options={
                'verbose_name': '系统后台管理员表信息',
                'verbose_name_plural': '系统后台管理员表信息',
                'db_table': 'sys_admin_info',
            },
        ),
        migrations.CreateModel(
            name='UserAdminInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('is_delete', models.CharField(choices=[('0', '正常'), ('1', '已删除')], default='0', max_length=1, verbose_name='删除标记(默认0未删除)')),
                ('data_exchange', models.CharField(default='0', max_length=1, verbose_name='数据交换位')),
                ('user_name', models.CharField(max_length=100, verbose_name='姓名')),
                ('user_account', models.CharField(max_length=50, verbose_name='登录用户名')),
                ('password', models.CharField(default='root', max_length=10, verbose_name='密码')),
                ('province', models.CharField(max_length=100, verbose_name='所在省')),
                ('province_code', models.CharField(max_length=50, verbose_name='所在省代码')),
                ('city', models.CharField(max_length=100, verbose_name='所在市')),
                ('city_code', models.CharField(max_length=50, verbose_name='所在市代码')),
                ('phone_number', models.CharField(max_length=12, verbose_name='手机号码')),
                ('identity_card', models.CharField(max_length=18, verbose_name='身份证号')),
                ('address', models.CharField(max_length=200, verbose_name='详细住址')),
                ('company', models.CharField(blank=True, max_length=100, null=True, verbose_name='公司名称')),
                ('sales', models.DecimalField(decimal_places=2, default=0, max_digits=20, verbose_name='销售总额')),
                ('registered_date', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('login_frequency', models.SmallIntegerField(verbose_name='登录次数')),
                ('recent_date', models.DateTimeField(auto_now=True, verbose_name='最近一次登录时间')),
                ('valid_status', models.CharField(choices=[('Y', '有效'), ('N', '无效')], default='Y', max_length=1, verbose_name='有效状态(默认Y有效)')),
            ],
            options={
                'verbose_name': '后台店铺用户信息表',
                'verbose_name_plural': '后台店铺用户信息表',
                'db_table': 'user_admin_info',
            },
        ),
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('is_delete', models.CharField(choices=[('0', '正常'), ('1', '已删除')], default='0', max_length=1, verbose_name='删除标记(默认0未删除)')),
                ('data_exchange', models.CharField(default='0', max_length=1, verbose_name='数据交换位')),
                ('user_name', models.CharField(max_length=100, verbose_name='姓名')),
                ('user_account', models.CharField(max_length=50, verbose_name='登录用户名')),
                ('password', models.CharField(default='1234@abcd', max_length=10, verbose_name='密码')),
                ('gender', models.CharField(choices=[('0', '男'), ('1', '女')], default='0', max_length=1, verbose_name='性别')),
                ('email', models.EmailField(max_length=50, verbose_name='电子邮箱')),
                ('phone_number', models.CharField(max_length=12, verbose_name='手机号码')),
                ('birthday', models.DateField(verbose_name='出生日期')),
                ('age', models.SmallIntegerField(verbose_name='年龄')),
                ('identity_card', models.CharField(max_length=18, verbose_name='身份证号')),
                ('origin', models.CharField(max_length=50, verbose_name='籍贯')),
                ('address', models.CharField(max_length=200, verbose_name='详细住址')),
                ('company', models.CharField(blank=True, max_length=100, null=True, verbose_name='所在公司名称')),
                ('account', models.DecimalField(decimal_places=2, default=0, max_digits=20, verbose_name='账户余额')),
                ('registered_date', models.DateTimeField(auto_now_add=True, verbose_name='注册时间')),
                ('recent_date', models.DateTimeField(auto_now=True, verbose_name='最近一次登录时间')),
                ('valid_status', models.CharField(choices=[('Y', '有效'), ('N', '无效')], default='Y', max_length=1, verbose_name='有效状态(默认Y有效)')),
            ],
            options={
                'verbose_name': '注册用户信息表',
                'verbose_name_plural': '注册用户信息表',
                'db_table': 'user_info',
            },
        ),
    ]
