from django.utils import timezone
from typing import List

# Models
from ..models import Category

import logging
logger = logging.getLogger(__name__)


def get_categories() -> List[Category]:
    """Fetch all categories."""
    categories = Category.objects.all()
    logger.info(f"{categories} fetched")
    return categories


def get_category_by_id(category_id: int) -> Category:
    """Fetch a category by its ID."""
    category = Category.objects.filter(id=category_id).first()
    logger.info(f"{category} fetched")
    return category


def delete_category(category: Category) -> Category:
    """Delete a category."""
    logger.info(f"{category} will be deleted.")
    category.delete()
    logger.info(f"{category} has been deleted.")
    return category


def create_category(name: str, description: str) -> Category:
    """Create a new category."""

    category = Category.objects.create(
        name=name,
        description=description
    )
    category.save()
    logger.info(f"\"{category}\" has been created")
    return category


def update_category(
        category: Category,
        name: str,
        description: str
) -> Category:
    """Update an existing category."""

    category.name = name
    category.description = description
    category.updated_at = timezone.now()

    category.save()
    logger.info(f"\"{category}\" has been updated")

    return category
