from typing import List

# Models
from django.contrib.auth.models import User

# Django
from django.contrib.auth.hashers import make_password

import logging
logger = logging.getLogger(__name__)


def get_users() -> List[User]:
    users = User.objects.all().order_by('id')
    logger.info(f"{users} fetched")
    return users


def get_user_by_id(user_id: int) -> User:
    user = User.objects.filter(id=user_id).first()
    logger.info(f"{user} fetched")
    return user


def delete_user(user: User) -> User:
    user.delete()
    logger.info(f"{user} has been deleted.")
    return user


def create_user(
    username: str,
    first_name: str,
    last_name: str,
    email: str,
    password: str
) -> User:
    # validated_data['password'] = make_password(validated_data['password'])
    # return User.objects.create(**validated_data)
    user = User.objects.create(
        username=username,
        first_name=first_name,
        last_name=last_name,
        email=email,
        password=make_password(password)
    )
    logger.info(f"\"{user}\" has been created.")
    return user


def update_user(
        user: User,
        username: str,
        first_name: str,
        last_name: str,
        email: str,
        password: str
) -> User:
    user.username = username
    user.first_name = first_name
    user.last_name = last_name
    user.email = email
    user.password = make_password(password)
    user.save()

    logger.info(f"\"{user}\" has been updated.")
    return user

