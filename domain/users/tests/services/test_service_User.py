from django.test import TestCase

from ..utils.utils import create_user_test

from ...services.service_User import get_users, get_user_by_id, \
    delete_user, create_user, update_user


# Create your tests here.
class ServiceUserGetUsersTestCase(TestCase):

    def test_should_be_able_to_get_all_users(self):
        """Should return all users"""
        user = create_user_test()
        users = get_users()
        self.assertIn(user, users)


class ServiceUserGetUserByIdTestCase(TestCase):

    def test_should_be_able_to_get_user_by_id(self):
        """Should be able to get user object by id"""
        user = create_user_test()
        user = get_user_by_id(user.pk)
        self.assertTrue(user)

    def test_should_return_none_if_user_id_do_not_exist(self):
        """Should return None if user id do not exist"""
        create_user_test()
        not_existing_user_id = 999
        user = get_user_by_id(not_existing_user_id)
        self.assertIsNone(user)


class ServiceUserDeleteUserByObjectTestCase(TestCase):

    def test_should_be_able_to_delete_user(self):
        """Should be able to delete user by object"""
        user = create_user_test()
        deleted_user_object = delete_user(user)
        self.assertEqual(user, deleted_user_object)


class ServiceUserCreateUserTestCase(TestCase):

    def test_should_be_able_create_user(self):
        """Should be able to create a user"""
        user = create_user(
            'root',
            'Super',
            'Admin',
            'root@old.st',
            '09106850351'
        )
        self.assertEqual({
            'username': 'root',
            'first_name': 'Super',
            'last_name': 'Admin',
            'email': 'root@old.st'
        }, {
            'username': user.username,
            'first_name': user.first_name,
            'last_name': user.last_name,
            'email': user.email,
        })


class ServiceUserUpdateUserTestCase(TestCase):

    def test_should_be_able_to_update_user(self):
        """Should be able to update a user"""
        user = create_user_test()
        update_user_object = update_user(
            user,
            'root2',
            'Super2',
            'Admin2',
            'root2@old.st',
            '09106850352'
        )
        self.assertEqual({
            'username': 'root2',
            'first_name': 'Super2',
            'last_name': 'Admin2',
            'email': 'root2@old.st'
        }, {
            'username': update_user_object.username,
            'first_name': update_user_object.first_name,
            'last_name': update_user_object.last_name,
            'email': update_user_object.email,
        })
