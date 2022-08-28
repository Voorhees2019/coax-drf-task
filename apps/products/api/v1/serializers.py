from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator

from apps.products.models import Product


class ProductSerializers(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"
        validators = [
            UniqueTogetherValidator(
                queryset=Product.objects.all(),
                fields=["name", "price"],
                message="Item with the such name and price already exists.",
            ),
        ]
