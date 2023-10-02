# Tests
from django.test import TestCase
from rest_framework.test import APIClient

from domain.users.tests.utils.utils import create_user_test, generate_token

# Models
from domain.stores.models import Store

import logging

logger = logging.getLogger(__name__)


class UsersIdProfileAPIViewGetTestCase(TestCase):

    def test_should_return_404_for_getting_not_existing_user(self):
        """Should return 404 for getting not existing user"""
        create_user_test()
        access_token = generate_token()

        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION=f'Bearer {access_token}')
        not_existing_user_id = 999
        path = f"/user-management/users/{not_existing_user_id}/stores"
        response = client.get(path)

        self.assertEqual(404, response.status_code)

    def test_should_be_able_get_a_user_with_stores(self):
        """Should be able to get a user with stores"""
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
        path = f"/user-management/users/{user.pk}/stores"
        response = client.get(path)
        content = response.json()

        self.assertEqual({
            'id': content['id'],
            'username': 'root',
            'first_name': 'Super',
            'last_name': 'Admin',
            'email': 'root@old.st',
            'stores': [{
                'id': store.id,
                'name': 'Apple Store',
                'contact_number': '09106850351',
                'address': 'California',
                'created_at': str(store.created_at.strftime("%Y-%m-%dT%H:%M:%S.%fZ")),
                'updated_at': str(store.updated_at.strftime("%Y-%m-%dT%H:%M:%S.%fZ"))
            }]
        }, content)

