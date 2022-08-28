from django_filters import rest_framework as django_filters
from rest_framework import filters
from rest_framework.generics import ListCreateAPIView
from rest_framework.pagination import PageNumberPagination

from apps.orders.models import Order

from .filters import OrderFilter
from .serializers import OrderSerializers


class OrderListCreateView(ListCreateAPIView):
    """A simple view for getting list of orders and creating a new order."""

    queryset = Order.objects.all()
    serializer_class = OrderSerializers
    pagination_class = PageNumberPagination
    filter_backends = [
        django_filters.DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter,
    ]
    filterset_class = OrderFilter
    search_fields = ["product__name", "product__description"]
    ordering_fields = ["product__name", "product__price"]
