from django.db import models
from db.base_model import BaseModel
from utils import options


class SysCodeTablesManage(BaseModel):
    """公共代码表管理"""
    code_table = models.CharField(verbose_name="代码表", max_length=10)
    code_table_name = models.CharField(verbose_name="代码表名称", max_length=50)
    valid_status = models.CharField(verbose_name="有效状态(默认Y有效)", choices=options.valid_choose, default='Y', max_length=1)

    class Meta:
        """公共代码表管理"""
        db_table = 'sys_code_tables_manage'
        verbose_name = '系统码表'
        verbose_name_plural = verbose_name

# 公共代码表相应值表


class SysCodeTables(BaseModel):
    """公共代码表相应值"""
    code = models.CharField(verbose_name="代码值", max_length=10)
    name = models.CharField(verbose_name="相应名称", max_length=100)
    code_table = models.CharField(verbose_name="代码表名", max_length=10)
    valid_status = models.CharField(verbose_name="有效状态(默认Y有效)", choices=options.valid_choose, default='Y', max_length=1)

    class Meta:
        """共代码表相应值"""
        # managed=False 表示不生成相应的表
        db_table = 'sys_code_tables'
        verbose_name = '公共代码表值'
        verbose_name_plural = verbose_name

# 系统行政区划代码表


class SysRegionalism(BaseModel):
    """系统行政区划代码表"""
    code = models.CharField(verbose_name="行政区划代码", max_length=10)
    name = models.CharField(verbose_name="行政区划名称", max_length=100)
    parent_node = models.CharField(verbose_name="父节点", max_length=10)
    valid_status = models.CharField(verbose_name="有效状态(默认Y有效)", choices=options.valid_choose, default='Y', max_length=1)

    class Meta:
        """系统行政区划代码表"""
        db_table = 'sys_regionalism'
        verbose_name = '系统行政区划代码表'
        verbose_name_plural = verbose_name

# 系统操作日志信息表


class SysOperationLog(BaseModel):
    """系统操作日志信息表"""
    operator_id = models.CharField(verbose_name="操作人id", max_length=100)
    operator = models.CharField(verbose_name="操作人", max_length=100)
    operator_account = models.CharField(verbose_name="操作账号", max_length=100)
    operator_time = models.DateTimeField(verbose_name="操作时间", auto_now_add=True)
    ipaddress = models.GenericIPAddressField(verbose_name="IP地址")
    content = models.CharField(verbose_name="操作内容", max_length=1000)

    class Meta:
        """系统操作日志信息表"""
        db_table = 'sys_operate_log'
        verbose_name = '系统操作日志信息表'
        verbose_name_plural = verbose_name


class SysMenu(BaseModel):
    """系统菜单表"""
    menu_name = models.CharField(verbose_name="菜单名称", max_length=100)
    menu_code = models.CharField(verbose_name="菜单编号", max_length=20)
    menu_level = models.CharField(verbose_name="菜单级别", choices=options.menu_level, default='1', max_length=2)
    menu_parent_code = models.CharField(verbose_name="菜单父级编号", default='0', max_length=20, null=True, blank=True)
    menu_url = models.CharField(verbose_name="菜单路径", max_length=200, null=True, blank=True)
    menu_img = models.CharField(verbose_name="菜单图片路径", max_length=200, null=True, blank=True)
    menu_status = models.CharField(verbose_name="菜单有效状态(默认Y有效)", choices=options.valid_choose, default='Y', max_length=1)

    class Meta:
        """系统菜单表"""
        db_table = 'sys_menu'
        verbose_name = '系统菜单表'
        verbose_name_plural = verbose_name


class SysRole(BaseModel):
    """系统角色表"""
    role_name = models.CharField(verbose_name="角色名称", max_length=100)
    role_describe = models.CharField(verbose_name='角色描述', max_length=500, null=True, blank=True)
    role_status = models.CharField(verbose_name="角色状态", choices=options.valid_choose, default='Y', max_length=1)

    class Meta:
        """系统角色表"""
        db_table = 'sys_role'
        verbose_name = '系统角色表'
        verbose_name_plural = verbose_name


class SysRoleMenu(BaseModel):
    """系统角色菜单关系表"""
    role_id = models.CharField(verbose_name="角色ID", max_length=50)
    menu_id = models.CharField(verbose_name="菜单ID", max_length=50)

    class Meta:
        """系统角色菜单关系表"""
        db_table = 'sys_role_menu'
        verbose_name = '系统角色菜单关系表'
        verbose_name_plural = verbose_name


class SysUserRole(BaseModel):
    """系统用户角色关系表"""
    user_id = models.CharField(verbose_name="用户ID", max_length=50)
    role_id = models.CharField(verbose_name="角色ID", max_length=50)

    class Meta:
        """系统用户角色关系表"""
        db_table = 'sys_user_role'
        verbose_name = '系统用户角色关系表'
        verbose_name_plural = verbose_name
