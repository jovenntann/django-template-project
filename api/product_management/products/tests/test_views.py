# Tests
from django.test import TestCase
from rest_framework.test import APIClient

from domain.users.tests.utils.utils import create_user_test, generate_token
from domain.stores.tests.utils.test_utils_Store import create_store_test
from domain.products.tests.utils.test_utils_Category import create_category_test
from domain.products.tests.utils.test_utils_Product import create_product_test

import logging

logger = logging.getLogger(__name__)


class ProductsAPIViewCreateTestCase(TestCase):

    def test_should_be_able_to_post_a_product(self):
        """Should be able to post a product"""
        user = create_user_test()
        store = create_store_test(user)
        category = create_category_test()

        access_token = generate_token()

        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION=f'Bearer {access_token}')
        path = '/product-management/products'
        data = {
            'store': store.id,
            'categories': category.id,
            'title': 'iPhone',
            'description': 'Best Phone',
        }
        response = client.post(path, data)
        actual_values = response.json()
        expected_values = {
            'id': actual_values['id'],
            'store': store.id,
            'categories': [{
                'id': category.id,
                'name': category.name,
                'description': category.description,
                'created_at': str(category.created_at.strftime("%Y-%m-%dT%H:%M:%S.%fZ")),
                'updated_at': str(category.updated_at.strftime("%Y-%m-%dT%H:%M:%S.%fZ")),
            }],
            'title': 'iPhone',
            'description': 'Best Phone',
            'created_at': actual_values['created_at'],
            'updated_at': actual_values['updated_at']
        }
        self.assertDictEqual(expected_values, actual_values)


class ProductsAPIViewGetTestCase(TestCase):

    def test_should_be_able_to_get_all_products(self):
        """Should be able to get all products"""
        user = create_user_test()
        store = create_store_test(user)
        category = create_category_test()
        product = create_product_test(store, category)

        access_token = generate_token()

        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION=f'Bearer {access_token}')
        path = '/product-management/products'
        response = client.get(path)
        actual_values = response.json()['results']

        expected_values = {
            'id': product.id,
            'store': store.id,
            'categories': [{
                "id": category.id,
                "name": category.name,
                "description": category.description,
                'created_at': str(category.created_at.strftime("%Y-%m-%dT%H:%M:%S.%fZ")),
                'updated_at': str(category.updated_at.strftime("%Y-%m-%dT%H:%M:%S.%fZ")),
            }],
            'title': 'iPhone',
            'description': 'Best Phone',
            'created_at': str(product.created_at.strftime("%Y-%m-%dT%H:%M:%S.%fZ")),
            'updated_at': str(product.updated_at.strftime("%Y-%m-%dT%H:%M:%S.%fZ")),
        }
        self.assertIn(expected_values, actual_values)
