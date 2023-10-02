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
