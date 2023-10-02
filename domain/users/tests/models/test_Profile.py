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