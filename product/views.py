from django.db import connection
from django.http import JsonResponse
from django.views import View
from rest_framework import viewsets
from .models import Product
from .serializers import ProductSerializer  # 导入序列化器


class ProductView(View):
    def get(self, request, product_id):
        with connection.cursor() as cursor:
            # 执行原生SQL查询，使用左连接查询产品和其所属的分类
            cursor.execute("""
                SELECT
                    p.id AS product_id,
                    p.name AS product_name,
                    c.id AS category_id,
                    c.name AS category_name
                FROM
                    tbl_product p
                LEFT JOIN
                    tbl_category c ON p.category_id = c.id
                WHERE
                    p.id = %s
            """, [product_id])

            row = cursor.fetchone()

            if row:
                # 构建产品数据字典
                product_data = {
                    'id': row[0],  # 产品ID
                    'name': row[1],  # 产品名称
                    'category': {
                        'id': row[2] if row[2] is not None else None,  # 类别ID
                        'name': row[3] if row[3] is not None else None,  # 类别名称
                    }
                }
                return JsonResponse(product_data)
            else:
                return JsonResponse({'error': 'Product not found'}, status=404)


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
