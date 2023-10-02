---
#### domain/users/tests/services/test_service_User.py
```
from django.test import TestCase

from ..utils.utils import create_user_test

from ...services.service_User import get_users, get_user_by_id, \
    delete_user, create_user, update_user


# Create your tests here.
class ServiceUserGetUsersTestCase(TestCase):

    def test_should_be_able_to_get_all_users(self):
        """Should return all users"""
        user = create_user_test()
        users = get_users()
        self.assertIn(user, users)


class ServiceUserGetUserByIdTestCase(TestCase):

    def test_should_be_able_to_get_user_by_id(self):
        """Should be able to get user object by id"""
        user = create_user_test()
        user = get_user_by_id(user.pk)
        self.assertTrue(user)

    def test_should_return_none_if_user_id_do_not_exist(self):
        """Should return None if user id do not exist"""
        create_user_test()
        not_existing_user_id = 999
        user = get_user_by_id(not_existing_user_id)
        self.assertIsNone(user)


class ServiceUserDeleteUserByObjectTestCase(TestCase):

    def test_should_be_able_to_delete_user(self):
        """Should be able to delete user by object"""
        user = create_user_test()
        deleted_user_object = delete_user(user)
        self.assertEqual(user, deleted_user_object)


class ServiceUserCreateUserTestCase(TestCase):

    def test_should_be_able_create_user(self):
        """Should be able to create a user"""
        user = create_user(
            'root',
            'Super',
            'Admin',
            'root@old.st',
            '09106850351'
        )
        self.assertEqual({
            'username': 'root',
            'first_name': 'Super',
            'last_name': 'Admin',
            'email': 'root@old.st'
        }, {
            'username': user.username,
            'first_name': user.first_name,
            'last_name': user.last_name,
            'email': user.email,
        })


class ServiceUserUpdateUserTestCase(TestCase):

    def test_should_be_able_to_update_user(self):
        """Should be able to update a user"""
        user = create_user_test()
        update_user_object = update_user(
            user,
            'root2',
            'Super2',
            'Admin2',
            'root2@old.st',
            '09106850352'
        )
        self.assertEqual({
            'username': 'root2',
            'first_name': 'Super2',
            'last_name': 'Admin2',
            'email': 'root2@old.st'
        }, {
            'username': update_user_object.username,
            'first_name': update_user_object.first_name,
            'last_name': update_user_object.last_name,
            'email': update_user_object.email,
        })

```

#### domain/stores/tests/services/test_service_Store.py
```
from django.test import TestCase

from ...models import Store

# Utils
from domain.users.tests.utils.utils import create_user_test

# Services
from ...services.service_Store import get_stores, get_store_by_id, create_store, delete_store, update_store

import logging
logger = logging.getLogger(__name__)


# Create your tests here.
class ServiceStoreGetStoresTestCase(TestCase):

    def test_should_be_able_to_get_all_stores(self):
        """Should return all Stores"""
        user = create_user_test()
        store = Store.objects.create(
            user=user,
            name="Apple Store",
            contact_number="09062131607",
            address="California"
        )

        stores = get_stores()

        expected_values = {
            'id': store.id,
            'name': store.name,
            'contact_number': store.contact_number,
            'address': store.address,
            'created_at': store.created_at,
            'updated_at': store.updated_at
        }
        actual_values = {
            'id': stores[0].id,
            'name': stores[0].name,
            'contact_number': stores[0].contact_number,
            'address': stores[0].address,
            'created_at': stores[0].created_at,
            'updated_at': stores[0].updated_at
        }
        self.assertDictEqual(expected_values, actual_values)


class ServiceStoreCreateStoreTestCase(TestCase):

    def test_should_be_able_create_store(self):
        """Should be able to create a store"""
        user = create_user_test()
        store = create_store(
            user,
            'Apple Store',
            '09062131607',
            'California'
        )

        expected_values = {
            'id': store.id,
            'name': 'Apple Store',
            'contact_number': '09062131607',
            'address': 'California',
            'created_at': store.created_at,
            'updated_at': store.updated_at
        }
        actual_values = {
            'id': store.id,
            'name': store.name,
            'contact_number': store.contact_number,
            'address': store.address,
            'created_at': store.created_at,
            'updated_at': store.updated_at
        }
        self.assertDictEqual(expected_values, actual_values)


class ServiceStoreGetStoreByIdTestCase(TestCase):

    def test_should_return_none_if_category_id_do_not_exist(self):
        """Should return None if category id do not exist"""
        user = create_user_test()
        Store.objects.create(
            user=user,
            name="Apple Store",
            contact_number="09062131607",
            address="California"
        )
        not_existing_store_id = 99
        store = get_store_by_id(not_existing_store_id)
        self.assertIsNone(store)

    def test_should_be_able_to_get_store_by_id(self):
        """Should be able to get store object by id"""
        user = create_user_test()
        store = Store.objects.create(
            user=user,
            name="Apple Store",
            contact_number="09062131607",
            address="California"
        )
        store_by_id = get_store_by_id(store.id)
        expected_values = {
            'id': store.id,
            'name': 'Apple Store',
            'contact_number': '09062131607',
            'address': 'California',
            'created_at': store.created_at,
            'updated_at': store.updated_at
        }
        actual_values = {
            'id': store_by_id.id,
            'name': store_by_id.name,
            'contact_number': store_by_id.contact_number,
            'address': store_by_id.address,
            'created_at': store_by_id.created_at,
            'updated_at': store_by_id.updated_at
        }
        self.assertDictEqual(expected_values, actual_values)


class ServiceStoreDeleteStoreByObjectTestCase(TestCase):

    def test_should_be_able_to_delete_category(self):
        """Should be able to delete store by object"""
        user = create_user_test()
        store = Store.objects.create(
            user=user,
            name="Apple Store",
            contact_number="09062131607",
            address="California"
        )
        deleted_store = delete_store(store)
        self.assertEqual(store, deleted_store)


class ServiceProductUpdateProductByObjectTestCase(TestCase):

    def test_should_be_able_update_product(self):
        """Should be able to update a product"""
        user = create_user_test()
        store = Store.objects.create(
            user=user,
            name="Apple",
            contact_number="09106850351",
            address="California"
        )

        updated_store = update_store(
            store,
            user,
            'Samsung Store',
            '09239108311',
            'Los Angeles'
        )

        expected_values = {
            'id': store.id,
            'user': user.pk,
            'name': 'Samsung Store',
            'contact_number': '09239108311',
            'address': 'Los Angeles',
            'created_at': store.created_at,
            'updated_at': store.updated_at
        }
        actual_values = {
            'id': updated_store.id,
            'user': updated_store.user.pk,
            'name': updated_store.name,
            'contact_number': updated_store.contact_number,
            'address': updated_store.address,
            'created_at': updated_store.created_at,
            'updated_at': updated_store.updated_at
        }
        self.assertDictEqual(expected_values, actual_values)

```

#### domain/products/services/service_Category.py
```
from django.utils import timezone
from typing import List

# Models
from ..models import Category

import logging
logger = logging.getLogger(__name__)


def get_categories() -> List[Category]:
    categories = Category.objects.all()
    logger.info(f"{categories} fetched")
    return categories


def get_category_by_id(category_id: int) -> Category:
    category = Category.objects.filter(id=category_id).first()
    logger.info(f"{category} fetched")
    return category


def delete_category(category: Category) -> Category:
    category.delete()
    logger.info(f"{category} has been deleted.")
    return category


def create_category(name: str, description: str) -> Category:
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
    category.name = name
    category.description = description
    category.updated_at = timezone.now()

    category.save()
    logger.info(f"\"{category}\" has been updated")

    return category

```

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