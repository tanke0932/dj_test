from django.db import models
from django.db.models import SET


# Create your models here.


class Category(models.Model):
    """ 分类表"""
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "分类管理"
        verbose_name_plural = verbose_name
        db_table = "tbl_category"


class Product(models.Model):
    """ 产品表"""
    name = models.CharField(max_length=128)
    category = models.ForeignKey(Category, null=True, default=None, on_delete=SET(None))
    create_time = models.DateTimeField('创建时间', auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "产品管理"
        verbose_name_plural = verbose_name
        db_table = "tbl_product"
