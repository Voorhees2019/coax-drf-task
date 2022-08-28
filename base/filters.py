from django_filters import rest_framework as filters


class BaseFilter(filters.FilterSet):
    # {urlpath}/?created_at__gte={day}-{month}-{year}
    created_at__gte = filters.DateFilter(field_name="created_at", lookup_expr="gte")
    created_at__lte = filters.DateFilter(field_name="created_at", lookup_expr="lte")

    class Meta:
        abstract = True
