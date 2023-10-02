---
#### domain/products/services/service_Product.py
```
from django.utils import timezone
from typing import List

# Models
from ..models import Product, Category
from domain.stores.models import Store

import logging
logger = logging.getLogger(__name__)


def get_products() -> List[Product]:
    products = Product.objects.all().prefetch_related('categories')
    logger.info(f"{products} fetched")
    return products


def get_product_by_id(product_id: int) -> Product:
    product = Product.objects.filter(id=product_id).first()
    logger.info(f"{product} fetched")
    return product


def delete_product(product: Product) -> Product:
    product.delete()
    logger.info(f"{product} has been deleted.")
    return product


def create_product(
        store: Store,
        categories: List[Category],
        title: str,
        description: str
) -> Product:

    product = Product.objects.create(
        store=store,
        title=title,
        description=description
    )
    product.categories.set(categories)
    # NOTE: This is nice because this instance won't save if the categories.set failed :)
    product.save()

    logger.info(f"\"{product.title}\" has been created")

    return product


def update_product(
        product: Product,
        store: Store,
        categories: List[Category],
        title: str,
        description: str
) -> Product:
    product.store = store
    product.title = title
    product.description = description
    product.updated_at = timezone.now()

    if type(categories) == list:
        product.categories.set(categories)

    product.save()

    logger.info(f"\"{product}\" has been updated.")

    return product
```
