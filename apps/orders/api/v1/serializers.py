from rest_framework import serializers

from apps.orders.models import Order
from apps.products.models import Product
from apps.products.api.v1.serializers import ProductSerializers


class OrderSerializers(serializers.ModelSerializer):
    product_id = serializers.PrimaryKeyRelatedField(
        queryset=Product.objects.all(),
        required=True,
        source="product",
    )
    product_details = ProductSerializers(read_only=True, source="product")

    class Meta:
        model = Order
        fields = ("product_id", "product_details", "created_at")
