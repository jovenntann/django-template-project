from django.test import TestCase

from domain.stores.models import Store
from ...models import Category
from ...models import Product

from domain.users.tests.utils.utils import create_user_test

import logging
logger = logging.getLogger(__name__)


class ModelProductTestCase(TestCase):
    def test_should_be_able_to_create_product(self):
        """Should be able to create a product"""
        user = create_user_test()
        store = Store.objects.create(
            user=user,
            name="Apple",
            contact_number="+1023456789",
            address="California"
        )
        category = Category.objects.create(
            name="Phones",
            description="All kind of phones"
        )
        product = Product.objects.create(
            store=store,
            title="iPhone",
            description="Best Phone"
        )
        product.categories.set([category])
        product.save()

        expected_values = {
            'user': user.pk,
            'store': store.id,
            'categories': product.categories,
            'title': 'iPhone',
            'description': 'Best Phone',
            'created_at': product.created_at,
            'updated_at': product.updated_at
        }
        actual_values = {
            'user': user.pk,
            'store': store.id,
            'categories': product.categories,
            'title': product.title,
            'description': product.description,
            'created_at': product.created_at,
            'updated_at': product.updated_at
        }
        self.assertDictEqual(expected_values, actual_values)
