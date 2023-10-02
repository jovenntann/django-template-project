# Tests
from django.test import TestCase
from rest_framework.test import APIClient

# Models
from domain.users.models import Profile

# Test Utilities from Account
from domain.users.tests.utils.utils import create_user_test, generate_token

import logging

logger = logging.getLogger(__name__)


class UserAPIViewTestCase(TestCase):

    def test_authenticated_user_should_get_user_data(self):
        """Authenticated User should get its own user data"""
        user = create_user_test()
        access_token = generate_token()

        # Update Profile Data (Since it's already created from signals)
        profile = Profile.objects.get(user=user)
        profile.bio = "Biography"
        profile.location = "Manila"
        profile.birth_date = "1990-01-01"
        profile.save()

        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION=f'Bearer {access_token}')
        path = "/authenticated/user"
        response = client.get(path)
        actual_values = response.json()
        expected_values = {
            'id': user.pk,
            'username': 'root',
            'first_name': 'Super',
            'last_name': 'Admin',
            'email': 'root@old.st'
        }
        self.assertDictEqual(expected_values, actual_values)
