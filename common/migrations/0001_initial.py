# Generated by Django 3.2.13 on 2022-07-08 22:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SysCodeTables',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('is_delete', models.CharField(choices=[('0', '正常'), ('1', '已删除')], default='0', max_length=1, verbose_name='删除标记(默认0未删除)')),
                ('data_exchange', models.CharField(default='0', max_length=1, verbose_name='数据交换位')),
                ('code', models.CharField(max_length=10, verbose_name='代码值')),
                ('name', models.CharField(max_length=100, verbose_name='相应名称')),
                ('code_table', models.CharField(max_length=10, verbose_name='代码表名')),
                ('valid_status', models.CharField(choices=[('Y', '有效'), ('N', '无效')], default='Y', max_length=1, verbose_name='有效状态(默认Y有效)')),
            ],
            options={
                'verbose_name': '公共代码表值',
                'verbose_name_plural': '公共代码表值',
                'db_table': 'sys_code_tables',
            },
        ),
        migrations.CreateModel(
            name='SysCodeTablesManage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('is_delete', models.CharField(choices=[('0', '正常'), ('1', '已删除')], default='0', max_length=1, verbose_name='删除标记(默认0未删除)')),
                ('data_exchange', models.CharField(default='0', max_length=1, verbose_name='数据交换位')),
                ('code_table', models.CharField(max_length=10, verbose_name='代码表')),
                ('code_table_name', models.CharField(max_length=50, verbose_name='代码表名称')),
                ('valid_status', models.CharField(choices=[('Y', '有效'), ('N', '无效')], default='Y', max_length=1, verbose_name='有效状态(默认Y有效)')),
            ],
            options={
                'verbose_name': '系统码表',
                'verbose_name_plural': '系统码表',
                'db_table': 'sys_code_tables_manage',
            },
        ),
        migrations.CreateModel(
            name='SysMenu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('is_delete', models.CharField(choices=[('0', '正常'), ('1', '已删除')], default='0', max_length=1, verbose_name='删除标记(默认0未删除)')),
                ('data_exchange', models.CharField(default='0', max_length=1, verbose_name='数据交换位')),
                ('menu_name', models.CharField(max_length=100, verbose_name='菜单名称')),
                ('menu_code', models.IntegerField(max_length=20, verbose_name='菜单编号')),
                ('menu_level', models.CharField(choices=[('1', '一级菜单'), ('2', '二级菜单'), ('3', '三级菜单')], default='1', max_length=2, verbose_name='菜单级别')),
                ('menu_parent_code', models.CharField(blank=True, default='0', max_length=20, null=True, verbose_name='菜单父级编号')),
                ('menu_url', models.CharField(blank=True, max_length=200, null=True, verbose_name='菜单路径')),
                ('menu_img', models.CharField(blank=True, max_length=200, null=True, verbose_name='菜单图片路径')),
                ('menu_status', models.CharField(choices=[('Y', '有效'), ('N', '无效')], default='Y', max_length=1, verbose_name='菜单有效状态(默认Y有效)')),
            ],
            options={
                'verbose_name': '系统菜单表',
                'verbose_name_plural': '系统菜单表',
                'db_table': 'sys_menu',
            },
        ),
        migrations.CreateModel(
            name='SysOperationLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('is_delete', models.CharField(choices=[('0', '正常'), ('1', '已删除')], default='0', max_length=1, verbose_name='删除标记(默认0未删除)')),
                ('data_exchange', models.CharField(default='0', max_length=1, verbose_name='数据交换位')),
                ('operator_id', models.CharField(max_length=100, verbose_name='操作人id')),
                ('operator', models.CharField(max_length=100, verbose_name='操作人')),
                ('operator_account', models.CharField(max_length=100, verbose_name='操作账号')),
                ('operator_time', models.DateTimeField(auto_now_add=True, verbose_name='操作时间')),
                ('ipaddress', models.GenericIPAddressField(verbose_name='IP地址')),
                ('content', models.CharField(max_length=1000, verbose_name='操作内容')),
            ],
            options={
                'verbose_name': '系统操作日志信息表',
                'verbose_name_plural': '系统操作日志信息表',
                'db_table': 'sys_operate_log',
            },
        ),
        migrations.CreateModel(
            name='SysRegionalism',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('is_delete', models.CharField(choices=[('0', '正常'), ('1', '已删除')], default='0', max_length=1, verbose_name='删除标记(默认0未删除)')),
                ('data_exchange', models.CharField(default='0', max_length=1, verbose_name='数据交换位')),
                ('code', models.CharField(max_length=10, verbose_name='行政区划代码')),
                ('name', models.CharField(max_length=100, verbose_name='行政区划名称')),
                ('parent_node', models.CharField(max_length=10, verbose_name='父节点')),
                ('valid_status', models.CharField(choices=[('Y', '有效'), ('N', '无效')], default='Y', max_length=1, verbose_name='有效状态(默认Y有效)')),
            ],
            options={
                'verbose_name': '系统行政区划代码表',
                'verbose_name_plural': '系统行政区划代码表',
                'db_table': 'sys_regionalism',
            },
        ),
        migrations.CreateModel(
            name='SysRole',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('is_delete', models.CharField(choices=[('0', '正常'), ('1', '已删除')], default='0', max_length=1, verbose_name='删除标记(默认0未删除)')),
                ('data_exchange', models.CharField(default='0', max_length=1, verbose_name='数据交换位')),
                ('role_name', models.CharField(max_length=100, verbose_name='角色名称')),
                ('role_describe', models.CharField(blank=True, max_length=500, null=True, verbose_name='角色描述')),
                ('role_status', models.CharField(choices=[('Y', '有效'), ('N', '无效')], default='Y', max_length=1, verbose_name='角色状态')),
            ],
            options={
                'verbose_name': '系统角色表',
                'verbose_name_plural': '系统角色表',
                'db_table': 'sys_role',
            },
        ),
        migrations.CreateModel(
            name='SysRoleMenu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('is_delete', models.CharField(choices=[('0', '正常'), ('1', '已删除')], default='0', max_length=1, verbose_name='删除标记(默认0未删除)')),
                ('data_exchange', models.CharField(default='0', max_length=1, verbose_name='数据交换位')),
                ('role_id', models.CharField(max_length=50, verbose_name='角色ID')),
                ('menu_id', models.CharField(max_length=50, verbose_name='菜单ID')),
            ],
            options={
                'verbose_name': '系统角色菜单关系表',
                'verbose_name_plural': '系统角色菜单关系表',
                'db_table': 'sys_role_menu',
            },
        ),
        migrations.CreateModel(
            name='SysUserRole',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('is_delete', models.CharField(choices=[('0', '正常'), ('1', '已删除')], default='0', max_length=1, verbose_name='删除标记(默认0未删除)')),
                ('data_exchange', models.CharField(default='0', max_length=1, verbose_name='数据交换位')),
                ('user_id', models.CharField(max_length=50, verbose_name='用户ID')),
                ('role_id', models.CharField(max_length=50, verbose_name='角色ID')),
            ],
            options={
                'verbose_name': '系统用户角色关系表',
                'verbose_name_plural': '系统用户角色关系表',
                'db_table': 'sys_user_role',
            },
        ),
    ]
