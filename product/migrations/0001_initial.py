# Generated by Django 3.2 on 2023-09-16 04:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
            ],
            options={
                'verbose_name': '类型管理',
                'verbose_name_plural': '类型管理',
                'db_table': 'tbl_category',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('category', models.ForeignKey(default=None, null=True, on_delete=models.SET(None), to='product.category')),
            ],
            options={
                'verbose_name': '产品管理',
                'verbose_name_plural': '产品管理',
                'db_table': 'tbl_product',
            },
        ),
    ]
