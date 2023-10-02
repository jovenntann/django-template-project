from django.test import TestCase
from rest_framework.test import APIClient

# Utils
from domain.users.tests.utils.utils import create_user_test, generate_token

# Models
from domain.stores.models import Store

import logging

logger = logging.getLogger(__name__)


class StoresAPIViewCreateTestCase(TestCase):

    def test_should_be_able_to_create_a_store(self):
        """Should be able to create a store"""
        user = create_user_test()
        access_token = generate_token()

        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION=f'Bearer {access_token}')
        path = '/store-management/stores'
        data = {
            'name': 'Apple Store',
            'contact_number': '09062131607',
            'address': 'California'
        }
        response = client.post(path, data)
        actual_values = response.json()
        logger.info(actual_values)
        expected_values = {
            'id': actual_values['id'],
            'user': user.pk,
            'name': 'Apple Store',
            'contact_number': '09062131607',
            'address': 'California',
            'created_at': actual_values['created_at'],
            'updated_at': actual_values['updated_at']
        }
        self.assertDictEqual(expected_values, actual_values)
        
        
class StoresAPIViewGetTestCase(TestCase):

    def test_should_be_able_to_get_all_stores(self):
        """Should be able to get all the stores"""
        user = create_user_test()
        access_token = generate_token()

        store = Store.objects.create(
            user=user,
            name="Apple Store",
            contact_number="09062131607",
            address="California"
        )

        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION=f'Bearer {access_token}')
        path = '/store-management/stores'
        response = client.get(path)
        actual_values = response.json()['results']

        expected_values = {
            'id': store.id,
            'user': user.pk,
            'name': store.name,
            'contact_number': store.contact_number,
            'address': store.address,
            'created_at': str(store.created_at.strftime("%Y-%m-%dT%H:%M:%S.%fZ")),
            'updated_at': str(store.updated_at.strftime("%Y-%m-%dT%H:%M:%S.%fZ")),
        }
        self.assertIn(expected_values, actual_values)
