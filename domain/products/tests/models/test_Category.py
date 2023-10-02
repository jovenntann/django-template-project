from django.test import TestCase

from ...models import Category


import logging
logger = logging.getLogger(__name__)


# Create your tests here.
class ModelCategoryTestCase(TestCase):
    def test_should_be_able_to_create_category(self):
        """Should be able to create a category"""
        category = Category.objects.create(
            name='Shoes',
            description='All kind of shoes'
        )
        expected_values = {
            'id': category.id,
            'name': 'Shoes',
            'description': 'All kind of shoes',
            'created_at': category.created_at,
            'updated_at': category.updated_at
        }
        actual_values = {
            'id': category.id,
            'name': category.name,
            'description': category.description,
            'created_at': category.created_at,
            'updated_at': category.updated_at
        }
        self.assertDictEqual(expected_values, actual_values)
