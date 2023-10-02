from django.utils import timezone
from typing import List

# Models
from ..models import Product, Category
from domain.stores.models import Store

import logging
logger = logging.getLogger(__name__)


def get_products() -> List[Product]:
    """Fetch all products with related categories."""
    products = Product.objects.all().prefetch_related('categories')
    logger.info(f"{products} fetched")
    return products


def get_product_by_id(product_id: int) -> Product:
    """Fetch a product by its ID."""
    product = Product.objects.filter(id=product_id).first()
    logger.info(f"{product} fetched")
    return product


def delete_product(product: Product) -> Product:
    """Delete a product."""
    logger.info(f"{product} will be deleted.")
    product.delete()
    logger.info(f"{product} has been deleted.")
    return product


def create_product(
        store: Store,
        categories: List[Category],
        title: str,
        description: str
) -> Product:
    """Create a new product."""

    product = Product.objects.create(
        store=store,
        title=title,
        description=description
    )
    product.categories.set(categories)
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
    """Update an existing product."""

    product.store = store
    product.title = title
    product.description = description
    product.updated_at = timezone.now()

    if isinstance(categories, list):
        product.categories.set(categories)

    product.save()

    logger.info(f"\"{product}\" has been updated.")

    return product
