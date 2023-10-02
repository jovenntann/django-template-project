# Tests
from django.test import TestCase
from rest_framework.test import APIClient

from domain.users.tests.utils.utils import create_user_test, generate_token
from domain.stores.tests.utils.test_utils_Store import create_store_test
from domain.products.tests.utils.test_utils_Category import create_category_test
from domain.products.tests.utils.test_utils_Product import create_product_test

import logging

logger = logging.getLogger(__name__)


class ProductsIdAPIViewGetTestCase(TestCase):

    def test_should_return_404_for_getting_not_existing_product(self):
        """Should return 404 for getting not existing product"""
        create_user_test()
        access_token = generate_token()

        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION=f'Bearer {access_token}')
        not_existing_product_id = 10
        path = f"/product-management/products/{not_existing_product_id}"
        response = client.get(path)

        self.assertEqual(404, response.status_code)

    def test_should_be_able_get_a_product(self):
        """Should be able to get a product"""
        user = create_user_test()
        store = create_store_test(user)
        category = create_category_test()
        product = create_product_test(store, category)

        access_token = generate_token()

        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION=f'Bearer {access_token}')
        path = f"/product-management/products/{product.id}"
        response = client.get(path)
        actual_values = response.json()

        expected_values = {
            'id': product.id,
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
            'created_at': str(product.created_at.strftime("%Y-%m-%dT%H:%M:%S.%fZ")),
            'updated_at': str(product.updated_at.strftime("%Y-%m-%dT%H:%M:%S.%fZ")),
        }
        self.assertDictEqual(expected_values, actual_values)


class ProductsIdAPIViewDeleteTestCase(TestCase):

    def test_should_return_404_for_deleting_not_existing_product(self):
        """Should return 404 for deleting not existing product"""
        create_user_test()
        access_token = generate_token()

        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION=f'Bearer {access_token}')
        not_existing_product_id = 10
        path = f"/product-management/products/{not_existing_product_id}"
        response = client.delete(path)

        self.assertEqual(404, response.status_code)

    def test_should_be_able_delete_a_product(self):
        """Should be able to delete a product"""
        user = create_user_test()
        store = create_store_test(user)
        category = create_category_test()
        product = create_product_test(store, category)

        access_token = generate_token()

        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION=f'Bearer {access_token}')
        path = f"/product-management/products/{product.id}"
        response = client.delete(path)
        actual_values = response.json()
        logger.info(actual_values)
        expected_values = {
            'operation': 'delete',
            'domain': 'products',
            'model': 'Product',
            'data': {
                'id': product.id,
                'store': store.id,
                'categories': [{
                    "id": category.id,
                    "name": category.name,
                    "description": category.description,
                    'created_at': str(category.created_at.strftime("%Y-%m-%dT%H:%M:%S.%fZ")),
                    'updated_at': str(category.updated_at.strftime("%Y-%m-%dT%H:%M:%S.%fZ"))
                }],
                'title': 'iPhone',
                'description': 'Best Phone',
                'created_at': str(product.created_at.strftime("%Y-%m-%dT%H:%M:%S.%fZ")),
                'updated_at': str(product.updated_at.strftime("%Y-%m-%dT%H:%M:%S.%fZ"))
            }
        }
        self.assertDictEqual(expected_values, actual_values)


class ProductsIdAPIViewUpdateTestCase(TestCase):

    def test_should_return_404_for_updating_not_existing_product(self):
        """Should return 404 for updating not existing product"""
        create_user_test()
        access_token = generate_token()

        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION=f'Bearer {access_token}')
        not_existing_product_id = 10
        path = f"/product-management/products/{not_existing_product_id}"
        data = {
            'store': 1,
            'categories': 1,
            'title': 'Android',
            'description': 'Best Android',
        }
        response = client.put(path, data)

        self.assertEqual(404, response.status_code)

    def test_should_be_able_update_a_product(self):
        """Should be able to update a product"""
        user = create_user_test()
        store = create_store_test(user)
        category = create_category_test()
        product = create_product_test(store, category)

        access_token = generate_token()

        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION=f'Bearer {access_token}')
        path = f"/product-management/products/{product.id}"
        data = {
            'store': store.id,
            'categories': [category.id],
            'title': 'Android',
            'description': 'Best Android',
        }
        response = client.put(path, data)
        actual_values = response.json()
        expected_values = {
            'id': product.id,
            'store': store.id,
            'categories': [{
                "id": category.id,
                "name": category.name,
                "description": category.description,
                'created_at': str(category.created_at.strftime("%Y-%m-%dT%H:%M:%S.%fZ")),
                'updated_at': str(category.updated_at.strftime("%Y-%m-%dT%H:%M:%S.%fZ"))
            }],
            'title': 'Android',
            'description': 'Best Android',
            'created_at': str(product.created_at.strftime("%Y-%m-%dT%H:%M:%S.%fZ")),
            'updated_at': actual_values['updated_at']
        }
        self.assertDictEqual(expected_values, actual_values)


class ProductsIdAPIViewPatchTestCase(TestCase):

    def test_should_return_404_for_patching_not_existing_product(self):
        """Should return 404 for patching not existing product"""
        create_user_test()
        access_token = generate_token()

        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION=f'Bearer {access_token}')
        not_existing_product_id = 10
        path = f"/product-management/products/{not_existing_product_id}"
        data = {
            'store': 1,
            'categories': 1,
            'title': 'Android',
            'description': 'Best Android',
        }
        response = client.patch(path, data)

        self.assertEqual(404, response.status_code)

    def test_should_be_able_patch_a_product(self):
        """Should be able to patch a product"""
        user = create_user_test()
        store = create_store_test(user)
        category = create_category_test()
        product = create_product_test(store, category)

        access_token = generate_token()

        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION=f'Bearer {access_token}')
        path = f"/product-management/products/{product.id}"
        data = {
            'title': 'iPhone',
            'description': 'Best iPhone',
        }
        response = client.patch(path, data)
        actual_values = response.json()
        expected_values = {
            'id': product.id,
            'store': store.id,
            'categories': [{
                "id": category.id,
                "name": category.name,
                "description": category.description,
                'created_at': str(category.created_at.strftime("%Y-%m-%dT%H:%M:%S.%fZ")),
                'updated_at': str(category.updated_at.strftime("%Y-%m-%dT%H:%M:%S.%fZ"))
            }],
            'title': 'iPhone',
            'description': 'Best iPhone',
            'created_at': str(product.created_at.strftime("%Y-%m-%dT%H:%M:%S.%fZ")),
            'updated_at': actual_values['updated_at']
        }
        self.assertDictEqual(expected_values, actual_values)
