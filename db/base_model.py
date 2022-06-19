from django.db import models
from utils import options


class BaseModel(models.Model):
    """模型抽象基类(主要定义数据库表公共字段部分)"""
    create_time = models.DateTimeField(verbose_name="创建时间", auto_now_add=True)
    update_time = models.DateTimeField(verbose_name="更新时间", auto_now=True)
    is_delete = models.CharField(verbose_name="删除标记(默认0未删除)", choices=options.delete_choose, default='0', max_length=1)
    data_exchange = models.CharField(verbose_name="数据交换位", default='0', max_length=1)

    class Meta:
        # 标记该类为抽象模型类
        abstract = True

