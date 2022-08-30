from django_filters import rest_framework as django_filters
from rest_framework import filters, status, viewsets
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response

from apps.products.models import Product
from apps.products.tasks import update_product_csvfile

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

    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        update_product_csvfile.delay(serializer.data.get("id"))  # run celery task
        return Response(serializer.data, status=status.HTTP_201_CREATED)
