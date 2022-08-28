from rest_framework import serializers

from apps.orders.models import Order
from apps.products.api.v1.serializers import ProductSerializers
from apps.products.models import Product


class OrderSerializers(serializers.ModelSerializer):
    product_id = serializers.PrimaryKeyRelatedField(
        queryset=Product.objects.all(),
        required=True,
        source="product",
    )
    product_details = ProductSerializers(read_only=True, source="product")

    class Meta:
        model = Order
        fields = ("id", "product_id", "product_details", "created_at")
