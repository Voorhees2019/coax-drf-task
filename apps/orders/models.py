from django.db import models
from django.utils.translation import gettext as _
from apps.products.models import Product


class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="product_orders")
    created_at = models.DateTimeField(_("Date created"), auto_now_add=True)

    def __str__(self):
        return f"Order #{self.pk}"

    class Meta:
        ordering = ("-created_at",)
