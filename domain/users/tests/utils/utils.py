from rest_framework.test import APIClient

# Models
from django.contrib.auth.models import User, Group
from django.contrib.auth.hashers import make_password


def create_group_test(group: str) -> Group:
    group_object = Group.objects.create(name=group)
    return group_object


def create_user_test() -> User:
    user = User.objects.create(
        username="root",
        password=make_password('09106850351'),
        first_name="Super",
        last_name="Admin",
        email="root@old.st"
    )
    return user


def create_admin_user_test() -> User:
    user = User.objects.create(
        username="root",
        password=make_password('09106850351'),
        first_name="Super",
        last_name="Admin",
        email="root@old.st"
    )
    group_object = create_group_test('admin')
    user.groups.add(group_object)
    return user


def generate_token() -> str:
    client = APIClient()
    path = '/authentication/token/'
    data = {
        "username": "root",
        "password": "09106850351"
    }
    response = client.post(path, data)
    content = response.json()
    access_token = content['access']
    return access_token


def generate_refresh_token() -> str:
    client = APIClient()
    path = '/authentication/token/'
    data = {
        "username": "root",
        "password": "09106850351"
    }
    response = client.post(path, data)
    content = response.json()
    refresh_token = content['refresh']
    return refresh_token
