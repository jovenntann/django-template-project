# Tests
from django.test import TestCase
from rest_framework.test import APIClient

# Models
from domain.users.models import Profile

# Test Utilities from Account
from domain.users.tests.utils.utils import create_user_test, generate_token

import logging
logger = logging.getLogger(__name__)


class ProfileAPIViewTestCase(TestCase):

    def test_authenticated_user_should_get_profile_data(self):
        """Authenticated User should get its own profile data"""
        user = create_user_test()
        access_token = generate_token()

        # Update Profile Data (Since its already created from signals)
        profile = Profile.objects.get(user=user)
        profile.bio = "Biography"
        profile.location = "Manila"
        profile.birth_date = "1990-01-01"
        profile.save()

        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION=f'Bearer {access_token}')
        path = "/authenticated/profile"
        response = client.get(path)
        content = response.json()

        self.assertEqual({
            'id': profile.id,
            'user': profile.user.id,
            'bio': 'Biography',
            'location': 'Manila',
            'birth_date': '1990-01-01'
        }, content)

