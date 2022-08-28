from django_filters import rest_framework as django_filters
from rest_framework import filters, viewsets
from rest_framework.pagination import PageNumberPagination

from apps.products.models import Product

from .filters import ProductFilter
from .serializers import ProductSerializers


class ProductViewSet(viewsets.ModelViewSet):
    """ViewSet for viewing, creating, editing and deleting products."""

    queryset = Product.objects.all()
    serializer_class = ProductSerializers
    pagination_class = PageNumberPagination
    filter_backends = [
        django_filters.DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter,
    ]
    filterset_class = ProductFilter
    search_fields = ["name", "description"]
    ordering_fields = ["name", "price"]
