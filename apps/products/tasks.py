import csv
import os.path
from json import loads

from django.core.serializers import serialize

from apps.products.models import Product
from config.celery import app


@app.task
def update_product_csvfile(product_id: int, filename: str = "products_details.csv") -> None:
    """Add product to product list csv file."""

    product = Product.objects.get(pk=product_id)
    headers = [f.name for f in product._meta.fields]

    # write headers
    if not os.path.isfile(filename):
        with open(filename, "w") as file:
            writer = csv.writer(file)
            writer.writerow(headers)

    # write product's data to csv file
    with open(filename, "a") as file:
        writer = csv.DictWriter(file, fieldnames=headers)
        product_data = loads(serialize("json", [product]))[0]
        writer.writerow(product_data.get("fields") | {"id": product_id})


@app.task
def count_apple_products():
    """Count and print amount of apple products."""

    print(f'Amount of Apple products: {Product.objects.filter(name__contains="apple").count()}')
