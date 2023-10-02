from django.test import TestCase

# Utils
from ..utils.utils import create_user_test, create_admin_user_test

# Permissions
from ...permissions.permission_group import is_in_group, has_group_permission
from ...permissions.permission_group import IsAdminUser

import logging
logger = logging.getLogger(__name__)


# Create your tests here.
class PermissionsGroupIsInGroupTestCase(TestCase):

    def test_should_return_false_if_user_is_in_specific_groups(self):
        """Test that the is_in_group function returns False when the user is not in the specified group."""
        user = create_user_test()
        is_user_in_admin_group = is_in_group(user, 'admin')
        self.assertFalse(is_user_in_admin_group)

    def test_should_return_true_if_user_is_in_specific_groups(self):
        """Test that the is_in_group function returns True when the user is in the specified group."""
        user = create_admin_user_test()
        is_user_in_admin_group = is_in_group(user, 'admin')
        self.assertTrue(is_user_in_admin_group)


class PermissionsGroupHasGroupPermissionTestCase(TestCase):

    def test_should_return_none_if_user_not_in_group(self):
        """Should return None if the user is not in group"""
        user = create_user_test()
        user_has_group_permission = has_group_permission(user, 'admin')
        self.assertFalse(user_has_group_permission)

    def test_should_return_group_objects_if_user_is_in_group(self):
        """Should return Group Objects if the user is in group"""
        user = create_admin_user_test()
        user_has_group_permission = has_group_permission(user, 'admin')
        self.assertIsNotNone(user_has_group_permission)


# TODO: Find a way to test this
# class PermissionsGroupIsAdminUserTestCase(TestCase):
#
#     def test_should_return_false_if_user_is_not_in_admin_group(self):
#         """Should return False of the user is not in Admin group"""
#         user = create_admin_user_test()
#         is_admin_user = IsAdminUser.has_permission(user, request=None, view=None)
#         self.assertFalse(is_admin_user)
#
#     def test_should_return_true_if_user_is_admin(self):
#         """Should return True of the user is in Admin group"""
#         user = create_admin_user_test()
#         is_admin_user = IsAdminUser.has_permission(user, request=None, view=None)
#         self.assertTrue(is_admin_user)

