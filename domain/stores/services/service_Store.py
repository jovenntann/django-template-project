from django.utils import timezone
from typing import List

# Models
from django.contrib.auth.models import User
from ..models import Store

import logging
logger = logging.getLogger(__name__)


def get_stores() -> List[Store]:
    stores = Store.objects.all()
    logger.info(f"{stores} fetched")
    return stores


def create_store(
        user: User,
        name: str,
        contact_number: str,
        address: str
) -> Store:
    store = Store.objects.create(
        user=user,
        name=name,
        contact_number=contact_number,
        address=address
    )
    store.save()
    logger.info(f"\"{store}\" has been created")
    return store


def get_store_by_id(store_id: int) -> Store:
    store = Store.objects.filter(id=store_id).first()
    if store:
        logger.info(f"{store} fetched")
        return store
    return store


def delete_store(store: Store) -> Store:
    store.delete()
    logger.info(f"{store} has been deleted.")
    return store


def update_store(
        store: Store,
        user: User,
        name: str,
        contact_number: str,
        address: str
) -> Store:
    store.store = store
    store.user = user
    store.name = name
    store.contact_number = contact_number
    store.address = address
    store.updated_at = timezone.now()

    store.save()

    logger.info(f"\"{store}\" has been updated.")

    return store
