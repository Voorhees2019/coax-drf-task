from django.db import models
from django.utils.translation import gettext as _


class Product(models.Model):
    name = models.CharField(_("Name"), max_length=255)
    description = models.TextField(_("Description"), max_length=1024)
    price = models.DecimalField(_("price"), max_digits=8, decimal_places=2)
    created_at = models.DateTimeField(_("Date created"), auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ("-created_at",)
