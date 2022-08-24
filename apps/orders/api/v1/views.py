from rest_framework.generics import ListCreateAPIView
from rest_framework.pagination import PageNumberPagination

from apps.orders.models import Order
from .serializers import OrderSerializers


class OrderListCreateView(ListCreateAPIView):
    """A simple view for getting list of orders and creating a new order."""

    queryset = Order.objects.all()
    serializer_class = OrderSerializers
    pagination_class = PageNumberPagination
