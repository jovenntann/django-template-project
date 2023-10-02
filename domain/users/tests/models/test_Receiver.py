from django.test import TestCase

# Test Utilities from Account
from domain.users.tests.utils.utils import create_user_test

# Models
from ...models import Profile

import logging
logger = logging.getLogger(__name__)


# Create your tests here.
class ModelReceiverTestCase(TestCase):

    def test_should_create_profile_once_user_is_created(self):
        """Should create profile once user is created"""
        user = create_user_test()
        profile_object = Profile.objects.get(user=user)

        self.assertTrue(profile_object)
