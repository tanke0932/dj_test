from django.urls import path, include
from rest_framework.routers import DefaultRouter

from . import views
from .views import ProductViewSet, ProductView

router = DefaultRouter()
router.register(r'products', ProductViewSet)

urlpatterns = [
    path("product/<int:product_id>/", views.ProductView.as_view(), name="query_product_and_category"),
    path('', include(router.urls)),
]
