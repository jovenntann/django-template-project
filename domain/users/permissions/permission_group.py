from django.contrib.auth.models import Group
from rest_framework import permissions

import logging
logger = logging.getLogger(__name__)


def is_in_group(user, group_name):
    """
    Takes a user and a group name, and returns `True` if the user is in that group.
    """
    try:
        return Group.objects.get(name=group_name).user_set.filter(id=user.id).exists()
    except Group.DoesNotExist:
        return None


def has_group_permission(user, required_groups):
    return any([is_in_group(user, group_name) for group_name in required_groups])


# class IsLoggedInUserOrAdmin(permissions.BasePermission):
#     # group_name for super admin
#     required_groups = ['admin']
#
#     def has_object_permission(self, request, view, obj):
#         has_group_permission = _has_group_permission(request.user, self.required_groups)
#         if self.required_groups is None:
#             return False
#         return obj == request.user or has_group_permission


class IsAdminUser(permissions.BasePermission):
    required_groups = ['admin']

    def has_permission(self, request, view):
        logger.info("has_permission")
        _has_group_permission = has_group_permission(request.user, self.required_groups)
        return request.user and _has_group_permission

    # READ: for further details https://dipeshpaudel.com/django-rest-framework-permissions-example
    # def has_object_permission(self, request, view, obj):
    #     has_group_permission = _has_group_permission(request.user, self.required_groups)
    #     return request.user and has_group_permission


# class IsAdminOrModerator(permissions.BasePermission):
#     required_groups = ['admin', 'moderator']
#
#     def has_permission(self, request, view):
#         has_group_permission = _has_group_permission(request.user, self.required_groups)
#         return request.user and has_group_permission


# class IsAdminOrAnonymousUser(permissions.BasePermission):
#     required_groups = ['admin', 'anonymous']
#
#     def has_permission(self, request, view):
#         has_group_permission = _has_group_permission(request.user, self.required_groups)
#         return request.user and has_group_permission
