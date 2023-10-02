# Tests
from django.test import TestCase
from rest_framework.test import APIClient

from domain.users.tests.utils.utils import create_user_test, generate_token
from domain.products.tests.utils.test_utils_Category import create_category_test

import logging

logger = logging.getLogger(__name__)


class CategoriesAPIViewCreateTestCase(TestCase):

    def test_should_be_able_to_post_a_category(self):
        """Should be able to post a category"""
        create_user_test()
        access_token = generate_token()

        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION=f'Bearer {access_token}')
        path = '/product-management/categories'
        data = {
            'name': 'Phones',
            'description': 'All kind of phones'
        }
        response = client.post(path, data)
        actual_values = response.json()
        expected_values = {
            'id': actual_values['id'],
            'name': 'Phones',
            'description': 'All kind of phones',
            'created_at': actual_values['created_at'],
            'updated_at': actual_values['updated_at']
        }
        self.assertDictEqual(expected_values, actual_values)


class CategoriesAPIViewGetTestCase(TestCase):

    def test_should_be_able_to_get_all_categories(self):
        """Should be able to get all categories"""
        create_user_test()
        category = create_category_test()

        access_token = generate_token()

        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION=f'Bearer {access_token}')
        path = '/product-management/categories'
        response = client.get(path)
        actual_values = response.json()['results']
        logger.info(actual_values)

        expected_values = {
            'id': category.id,
            'name': 'Phones',
            'description': 'All kind of phones',
            'created_at': str(category.created_at.strftime("%Y-%m-%dT%H:%M:%S.%fZ")),
            'updated_at': str(category.updated_at.strftime("%Y-%m-%dT%H:%M:%S.%fZ")),
        }
        self.assertIn(expected_values, actual_values)
