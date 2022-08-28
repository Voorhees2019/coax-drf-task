import django_filters

from apps.orders.models import Order
from base.filters import BaseFilter


class OrderFilter(BaseFilter):
    product__description = django_filters.CharFilter(lookup_expr="icontains")

    class Meta:
        model = Order
        fields = {
            "id": ["exact"],  # {urlpath}/?id=
            "product__id": ["exact"],  # {urlpath}/?product__id=
            "product__name": ["exact"],  # {urlpath}/?product__name=
            "product__price": ["lt", "lte", "gt", "gte"],  # {urlpath}/?product__price__lt=
        }
