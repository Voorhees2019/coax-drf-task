import django_filters

from apps.products.models import Product
from base.filters import BaseFilter


class ProductFilter(BaseFilter):
    description = django_filters.CharFilter(lookup_expr="icontains")

    class Meta:
        model = Product
        fields = {
            "id": ["exact"],  # {urlpath}/?id=
            "name": ["exact"],  # {urlpath}/?name=
            "price": ["lt", "lte", "gt", "gte"],  # {urlpath}/?price__lt=
        }
