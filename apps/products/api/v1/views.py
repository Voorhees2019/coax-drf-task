from rest_framework import viewsets
from apps.products.models import Product
from .serializers import ProductSerializers
from rest_framework.pagination import PageNumberPagination


class ProductViewSet(viewsets.ModelViewSet):
    """ViewSet for viewing, creating, editing and deleting products."""

    queryset = Product.objects.all()
    serializer_class = ProductSerializers
    pagination_class = PageNumberPagination
