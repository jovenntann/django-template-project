---
#### domain/users/tests/models/test_Profile.py
```
from django.test import TestCase

# Test Utilities from Account
from domain.users.tests.utils.utils import create_user_test

# Models
from ...models import Profile

import logging
logger = logging.getLogger(__name__)


# Create your tests here.
class ModelProfileTestCase(TestCase):
    def should_be_able_to_create_profile(self):
        user = create_user_test()
        profile_object = Profile.objects.create(
            user=user,
            bio="Biography",
            location="Manila",
            birth_date="1990-01-01"
        )
        expected_values = {
            'bio': 'Biography',
            'location': 'Manila',
            'birth_date': '1990-01-01'
        }
        actual_values = {
            'bio': profile_object.bio,
            'location': profile_object.location,
            'birth_date': profile_object.birth_date
        }
        self.assertDictEqual(expected_values, actual_values)
```

#### domain/products/tests/models/test_Product.py
```
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

```

#### domain/products/tests/models/test_Category.py
```
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

```

#### domain/stores/tests/models/test_Store.py
```
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
```