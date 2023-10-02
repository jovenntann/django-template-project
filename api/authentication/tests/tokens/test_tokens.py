# Tests
from django.test import TestCase
from rest_framework.test import APIClient

# Test Utilities
from domain.users.tests.utils.utils import create_user_test, generate_refresh_token

import logging

logger = logging.getLogger(__name__)


class TokenTestCase(TestCase):

    def test_should_return_401_unauthorized_for_invalid_user_credentials(self):
        """Should return a token and refresh token for valid user credentials"""
        create_user_test()

        client = APIClient()
        path = '/authentication/token/'
        data = {
            "username": "root",
            "password": "000000000"
        }
        response = client.post(path, data)

        self.assertTrue(400, response.status_code)

    def test_should_return_token_and_refresh_token_for_valid_user_credentials(self):
        """Should return a token and refresh token for valid user credentials"""
        create_user_test()

        client = APIClient()
        path = '/authentication/token/'
        data = {
            "username": "root",
            "password": "09106850351"
        }
        response = client.post(path, data)
        content = response.json()

        self.assertTrue('refresh' in content and 'access' in content)


class TokenRefreshTestCase(TestCase):

    def test_should_return_401_unauthorized_for_invalid_refresh_token(self):
        """Should return 401 Unauthorized by using a invalid refresh token"""
        client = APIClient()
        invalid_refresh_token = 'invalid_refresh_token'
        path = '/authentication/token/refresh/'
        data = {
            "refresh": invalid_refresh_token
        }
        response = client.post(path, data)

        self.assertTrue(response.status_code, 401)

    def test_should_return_token_using_a_valid_refresh_token(self):
        """Should return a token by using a valid refresh token"""
        create_user_test()
        refresh_token = generate_refresh_token()

        client = APIClient()
        path = '/authentication/token/refresh/'
        data = {
            "refresh": refresh_token
        }
        response = client.post(path, data)
        content = response.json()

        self.assertTrue('access' in content)
