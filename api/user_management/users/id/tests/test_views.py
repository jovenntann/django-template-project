# Tests
from django.test import TestCase
from rest_framework.test import APIClient

from domain.users.tests.utils.utils import create_user_test, generate_token

import logging

logger = logging.getLogger(__name__)


class UsersIdAPIViewGetTestCase(TestCase):

    def test_should_return_404_for_getting_not_existing_user(self):
        """Should return 404 for getting not existing user"""
        create_user_test()
        access_token = generate_token()

        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION=f'Bearer {access_token}')
        not_existing_user_id = 999
        path = f"/user-management/users/{not_existing_user_id}"
        response = client.get(path)

        self.assertEqual(404, response.status_code)

    def test_should_be_able_get_a_user(self):
        """Should be able to get a user"""
        user = create_user_test()
        access_token = generate_token()

        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION=f'Bearer {access_token}')
        path = f"/user-management/users/{user.pk}"
        response = client.get(path)
        actual_values = response.json()
        expected_values = {
            'id': actual_values['id'],
            'username': 'root',
            'first_name': 'Super',
            'last_name': 'Admin',
            'email': 'root@old.st'
        }
        self.assertDictEqual(expected_values, actual_values)


class UsersIdAPIViewDeleteTestCase(TestCase):

    def test_should_return_404_for_deleting_not_existing_user(self):
        """Should return 404 for deleting not existing user"""
        create_user_test()
        access_token = generate_token()

        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION=f'Bearer {access_token}')
        not_existing_user_id = 999
        path = f"/user-management/users/{not_existing_user_id}"
        response = client.delete(path)

        self.assertEqual(404, response.status_code)

    def test_should_be_able_delete_a_user(self):
        """Should be able to delete a user"""
        user = create_user_test()
        access_token = generate_token()

        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION=f'Bearer {access_token}')
        path = f"/user-management/users/{user.pk}"
        response = client.delete(path)
        actual_values = response.json()
        expected_values = {
            'operation': 'delete',
            'domain': 'users',
            'model': 'User',
            'data': {
                'id': user.pk,
                'username': 'root',
                'first_name': 'Super',
                'last_name': 'Admin',
                'email': 'root@old.st'
            }
        }
        self.assertDictEqual(expected_values, actual_values)


class UsersIdAPIViewUpdateTestCase(TestCase):

    def test_should_return_404_for_updating_not_existing_user(self):
        """Should return 404 for updating not existing user"""
        create_user_test()
        access_token = generate_token()

        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION=f'Bearer {access_token}')
        not_existing_user_id = 999
        path = f"/user-management/users/{not_existing_user_id}"
        data = {
            "username": "root2",
            "password": "09106850350",
            'first_name': 'Super2',
            'last_name': 'Admin2',
            'email': 'root2@old.st'
        }
        response = client.put(path, data)

        self.assertEqual(404, response.status_code)

    def test_should_be_able_update_a_user(self):
        """Should be able to update a user"""
        user = create_user_test()
        access_token = generate_token()

        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION=f'Bearer {access_token}')
        path = f"/user-management/users/{user.pk}"
        data = {
            "username": "root2",
            "password": "09106850350",
            'first_name': 'Super2',
            'last_name': 'Admin2',
            'email': 'root2@old.st'
        }
        response = client.put(path, data)
        actual_values = response.json()
        expected_values = {
            'id': user.pk,
            'username': 'root2',
            'first_name': 'Super2',
            'last_name': 'Admin2',
            'email': 'root2@old.st'
        }
        self.assertDictEqual(expected_values, actual_values)


class UsersIdAPIViewPatchTestCase(TestCase):

    def test_should_return_404_for_patching_not_existing_user(self):
        """Should return 404 for patching not existing user"""
        create_user_test()
        access_token = generate_token()

        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION=f'Bearer {access_token}')
        not_existing_user_id = 999
        path = f"/user-management/users/{not_existing_user_id}"
        data = {
            'first_name': 'Super2',
            'last_name': 'Admin2'
        }
        response = client.patch(path, data)

        self.assertEqual(404, response.status_code)

    def test_should_be_able_patch_a_user(self):
        """Should be able to patch a user"""
        user = create_user_test()
        access_token = generate_token()

        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION=f'Bearer {access_token}')
        path = f"/user-management/users/{user.pk}"
        data = {
            'first_name': 'Super2',
            'last_name': 'Admin2',
        }
        response = client.patch(path, data)
        actual_values = response.json()
        expected_values = {
            'id': user.pk,
            'username': 'root',
            'first_name': 'Super2',
            'last_name': 'Admin2',
            'email': 'root@old.st'
        }
        self.assertDictEqual(expected_values, actual_values)
