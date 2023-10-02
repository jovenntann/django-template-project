from django.test import TestCase
from ...models import Store
from django.contrib.auth.models import User

import logging
logger = logging.getLogger(__name__)


# Create your tests here.
class ModelStoreTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create(username="root")
        self.store = Store.objects.create(
            user=self.user,
            name="Apple",
            contact_number="+1023456789",
            address="California"
        )

    # def tearDown(self):
    #     self.user.delete()
    #     self.store.delete()

    def test_get_excerpt(self):
        """Should return first few characters of the address"""
        result = self.store.get_excerpt(5)
        self.assertEqual('Calif', result)

    def test_store_str(self):
        self.assertEqual('Apple', str(self.store))

    def test_should_be_able_to_create_store(self):
        """Should be able to create a store"""
        store = Store.objects.create(
            user=self.user,
            name="Apple",
            contact_number="+1023456789",
            address="California"
        )

        expected_values = {
            'user': self.user.pk,
            'name': 'Apple',
            'contact_number': '+1023456789',
            'address': 'California'
        }
        actual_values = {
            'user': self.user.pk,
            'name': store.name,
            'contact_number': store.contact_number,
            'address': store.address
        }
        self.assertDictEqual(expected_values, actual_values)