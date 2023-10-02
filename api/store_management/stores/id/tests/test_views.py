# Tests
from django.test import TestCase
from rest_framework.test import APIClient

from domain.users.tests.utils.utils import create_user_test, generate_token

# Models
from domain.stores.models import Store

import logging

logger = logging.getLogger(__name__)


class StoresIdAPIViewGetTestCase(TestCase):

    def test_should_return_404_for_not_existing_store(self):
        """Should return 404 for not existing store"""
        create_user_test()
        access_token = generate_token()

        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION=f'Bearer {access_token}')
        not_existing_store_id = 999
        path = f"/store-management/stores/{not_existing_store_id}"
        response = client.get(path)

        self.assertEqual(404, response.status_code)

    def test_should_be_able_to_get_a_store(self):
        """Should be able to get a store"""
        user = create_user_test()
        store = Store.objects.create(
            user=user,
            name='Apple Store',
            contact_number='09106850351',
            address='California'
        )
        store.save()
        access_token = generate_token()

        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION=f'Bearer {access_token}')
        path = f"/store-management/stores/{store.id}"
        response = client.get(path)
        actual_values = response.json()

        expected_values = {
            'id': store.id,
            'user': user.pk,
            'name': 'Apple Store',
            'contact_number': '09106850351',
            'address': 'California',
            'created_at': str(store.created_at.strftime("%Y-%m-%dT%H:%M:%S.%fZ")),
            'updated_at': str(store.updated_at.strftime("%Y-%m-%dT%H:%M:%S.%fZ")),
        }
        self.assertDictEqual(expected_values, actual_values)


class StoresIdAPIViewDeleteTestCase(TestCase):

    def test_should_return_404_for_deleting_not_existing_store(self):
        """Should return 404 for deleting not existing store"""
        create_user_test()
        access_token = generate_token()

        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION=f'Bearer {access_token}')
        not_existing_store_id = 10
        path = f"/store-management/stores/{not_existing_store_id}"
        response = client.delete(path)
        self.assertEqual(404, response.status_code)

    def test_should_be_able_to_delete_a_store(self):
        """Should be able to delete a store"""
        user = create_user_test()
        store = Store.objects.create(
            user=user,
            name='Apple Store',
            contact_number='09106850351',
            address='California'
        )
        store.save()

        access_token = generate_token()

        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION=f'Bearer {access_token}')
        path = f"/store-management/stores/{store.id}"
        response = client.delete(path)
        actual_values = response.json()
        expected_values = {
            'operation': 'delete',
            'domain': 'stores',
            'model': 'Store',
            'data': {
                'id': store.id,
                'user': user.pk,
                'name': 'Apple Store',
                'contact_number': '09106850351',
                'address': 'California',
                'created_at': str(store.created_at.strftime("%Y-%m-%dT%H:%M:%S.%fZ")),
                'updated_at': str(store.updated_at.strftime("%Y-%m-%dT%H:%M:%S.%fZ"))
            }
        }
        self.assertDictEqual(expected_values, actual_values)


class StoresIdAPIViewUpdateTestCase(TestCase):

    def test_should_return_404_for_updating_not_existing_store(self):
        """Should return 404 for updating not existing store"""
        create_user_test()
        access_token = generate_token()

        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION=f'Bearer {access_token}')
        not_existing_store_id = 99
        path = f"/store-management/stores/{not_existing_store_id}"
        data = {
            'name': 'Samsung Store',
            'contact_number': '09239108311',
            'address': 'Los Angeles',
        }
        response = client.put(path, data)
        self.assertEqual(404, response.status_code)

    def test_should_be_able_to_update_a_store(self):
        """Should be able to update a store"""
        user = create_user_test()
        store = Store.objects.create(
            user=user,
            name='Apple Store',
            contact_number='09106850351',
            address='California'
        )

        access_token = generate_token()

        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION=f'Bearer {access_token}')
        path = f"/store-management/stores/{store.id}"
        data = {
            'name': 'Samsung Store',
            'contact_number': '09239108311',
            'address': 'Los Angeles',
        }
        response = client.put(path, data)
        actual_values = response.json()
        expected_values = {
            'id': store.id,
            'user': user.pk,
            'name': 'Samsung Store',
            'contact_number': '09239108311',
            'address': 'Los Angeles',
            'created_at': actual_values['created_at'],
            'updated_at': actual_values['updated_at']
        }
        self.assertDictEqual(expected_values, actual_values)


class StoresIdAPIViewPatchTestCase(TestCase):

    def test_should_return_404_for_patching_not_existing_store(self):
        """Should return 404 for patching not existing store"""
        create_user_test()
        access_token = generate_token()

        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION=f'Bearer {access_token}')
        not_existing_store_id = 999
        path = f"/store-management/stores/{not_existing_store_id}"
        data = {
            'name': 'Samsung Store',
            'contact_number': '09239108311',
            'address': 'Los Angeles',
        }
        response = client.patch(path, data)
        self.assertEqual(404, response.status_code)

    def test_should_be_able_to_patch_a_store(self):
        """Should be able to patched a store"""
        user = create_user_test()
        store = Store.objects.create(
            user=user,
            name='Apple Store',
            contact_number='09106850351',
            address='California'
        )

        access_token = generate_token()

        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION=f'Bearer {access_token}')
        path = f"/store-management/stores/{store.id}"
        data = {
            'name': 'Samsung Store',
            'contact_number': '09239108311',
            'address': 'Los Angeles',
        }
        response = client.patch(path, data)
        actual_values = response.json()
        expected_values = {
            'id': store.id,
            'user': user.pk,
            'name': 'Samsung Store',
            'contact_number': '09239108311',
            'address': 'Los Angeles',
            'created_at': actual_values['created_at'],
            'updated_at': actual_values['updated_at']
        }
        self.assertDictEqual(expected_values, actual_values)
