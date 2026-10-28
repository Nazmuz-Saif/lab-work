from decimal import Decimal

from django.core.validators import MinValueValidator, RegexValidator
from django.db import models


class Product(models.Model):
    product_code = models.CharField(
        max_length=20,
        primary_key=True,
        validators=[RegexValidator(r"^[A-Za-z0-9]+$", "Use only letters and digits.")],
    )
    product_name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(Decimal("0.01"))])

    class Meta:
        db_table = "Product"
        ordering = ["product_code"]
