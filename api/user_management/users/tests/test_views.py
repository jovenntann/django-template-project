# Tests
from django.test import TestCase
from rest_framework.test import APIClient

from domain.users.tests.utils.utils import create_user_test, create_admin_user_test, generate_token

import logging

logger = logging.getLogger(__name__)


class UsersAPIViewCreateTestCase(TestCase):

    def test_normal_user_should_not_be_able_to_create_a_user(self):
        """As a Normal User, I Should not be able to create a user"""
        create_user_test()
        access_token = generate_token()

        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION=f'Bearer {access_token}')
        path = '/user-management/users'
        data = {
            'username': 'juan',
            'password': 'Pass@12345',
            'first_name': 'Juan',
            'last_name': 'Dela Cruz',
            'email': 'juan@old.st'
        }
        response = client.post(path, data)
        actual_values = response.json()
        expected_values = {
            'detail': 'You do not have permission to perform this action.'
        }
        self.assertDictEqual(expected_values, actual_values)
        self.assertEqual(403, response.status_code)

    def test_admin_should_be_able_to_create_a_user(self):
        """As admin, I Should be able to create a user"""
        create_admin_user_test()
        access_token = generate_token()

        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION=f'Bearer {access_token}')
        path = '/user-management/users'
        data = {
            'username': 'juan',
            'password': 'Pass@12345',
            'first_name': 'Juan',
            'last_name': 'Dela Cruz',
            'email': 'juan@old.st'
        }
        response = client.post(path, data)
        actual_values = response.json()

        expected_values = {
            'id': actual_values['id'],
            'username': 'juan',
            'first_name': 'Juan',
            'last_name': 'Dela Cruz',
            'email': 'juan@old.st'
        }
        self.assertDictEqual(expected_values, actual_values)


class UsersAPIViewGetTestCase(TestCase):

    def test_normal_user_should_not_be_able_to_get_all_users(self):
        """As a Normal User, I Should not be able to get all users"""
        create_user_test()
        access_token = generate_token()

        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION=f'Bearer {access_token}')
        path = '/user-management/users'
        response = client.get(path)
        actual_values = response.json()
        expected_values = {
            'detail': 'You do not have permission to perform this action.'
        }
        self.assertDictEqual(expected_values, actual_values)
        self.assertEqual(403, response.status_code)

    def test_admin_should_get_all_users(self):
        """As admin, I Should be able to get all users"""
        user = create_admin_user_test()
        access_token = generate_token()

        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION=f'Bearer {access_token}')
        path = '/user-management/users'
        response = client.get(path)
        actual_values = response.json()['results']

        expected_values = {
            'id': user.pk,
            'username': 'root',
            'first_name': 'Super',
            'last_name': 'Admin',
            'email': 'root@old.st',
        }
        self.assertIn(expected_values, actual_values)
