# Tests
from django.test import TestCase
from rest_framework.test import APIClient

from domain.users.tests.utils.utils import create_user_test, generate_token

# Models
from domain.users.models import Profile

import logging

logger = logging.getLogger(__name__)


class UsersIdProfileAPIViewGetTestCase(TestCase):

    def test_should_return_404_for_getting_not_existing_user(self):
        """Should return 404 for getting not existing user"""
        create_user_test()
        access_token = generate_token()

        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION=f'Bearer {access_token}')
        not_existing_user_id = 999
        path = f"/user-management/users/{not_existing_user_id}/profile"
        response = client.get(path)

        self.assertEqual(404, response.status_code)

    def test_should_be_able_get_a_user_with_profile(self):
        """Should be able to get a user with profile"""
        user = create_user_test()
        access_token = generate_token()

        # Update Profile Data (Since its already created from signals)
        profile_object = Profile.objects.get(user=user)
        profile_object.bio = "Biography"
        profile_object.location = "Manila"
        profile_object.birth_date = "1990-01-01"
        profile_object.save()

        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION=f'Bearer {access_token}')
        path = f"/user-management/users/{user.pk}/profile"
        response = client.get(path)
        actual_values = response.json()
        expected_values = {
            'id': actual_values['id'],
            'username': 'root',
            'first_name': 'Super',
            'last_name': 'Admin',
            'email': 'root@old.st',
            'profile': {
                'id': profile_object.id,
                'user': user.pk,
                'bio': 'Biography',
                'location': 'Manila',
                'birth_date': '1990-01-01'
            }
        }
        self.assertDictEqual(expected_values, actual_values)
