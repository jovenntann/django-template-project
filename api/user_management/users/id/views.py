# DRF
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated

# Serializers
from .serializers import ReadUserSerializer, UpdateUserSerializer, DeleteUserSerializer

# Services
from domain.users.services.service_User import get_user_by_id, delete_user, update_user

# Django Shortcuts
from django.http import Http404

# Library: drf-yasg
from drf_yasg.utils import swagger_auto_schema

import logging
logger = logging.getLogger(__name__)


# TODO: User Permission (Cause this section might only useful for Administrator or Moderator)

class UsersIdAPIView(APIView):

    permission_classes = (IsAuthenticated,)

    @staticmethod
    @swagger_auto_schema(
        responses={
            200: ReadUserSerializer()
        },
        operation_description="description",
        operation_id="users_read.",
        tags=["user-management"],
    )
    def get(request, user_id=None):
        logger.info(f"authenticated: {request.user}")
        user = get_user_by_id(user_id)
        if user is None:
            raise Http404
        user_serializer = ReadUserSerializer(user)
        return Response(user_serializer.data)

    @staticmethod
    @swagger_auto_schema(
        operation_description="description",
        operation_id="users_delete",
        tags=["user-management"],
        responses={
            200: DeleteUserSerializer()
        }
    )
    def delete(request, user_id=None):
        logger.info(f"authenticated: {request.user}")
        user = get_user_by_id(user_id)
        if user is None:
            raise Http404
        # Copy user so that we can return this data from our delete response
        response = {
            'operation': 'delete',
            'domain': 'users',
            'model': 'User',
            'data': user
        }
        response_serializer = DeleteUserSerializer(response)
        response_serializer_data = response_serializer.data

        delete_user(user)

        return Response(response_serializer_data)

    @staticmethod
    @swagger_auto_schema(
        operation_description="description",
        operation_id="users_update",
        tags=["user-management"],
        request_body=UpdateUserSerializer,
        responses={
            200: ReadUserSerializer()
        }
    )
    def put(request, user_id=None):
        logger.info(f"authenticated: {request.user}")
        user = get_user_by_id(user_id)
        if user is None:
            raise Http404
        user_serializer = UpdateUserSerializer(
            data=request.data
        )
        user_serializer.is_valid(raise_exception=True)
        user = update_user(
            user,
            user_serializer.validated_data.get('username', user.username),
            user_serializer.validated_data.get('first_name', user.first_name),
            user_serializer.validated_data.get('last_name', user.last_name),
            user_serializer.validated_data.get('email', user.email),
            user_serializer.validated_data.get('password', user.password)
        )
        # NOTE: Re-serialize to fetch more detailed data
        user_serializer = ReadUserSerializer(user)
        return Response(user_serializer.data)

    @staticmethod
    @swagger_auto_schema(
        operation_description="description",
        operation_id="users_patch",
        tags=["user-management"],
        request_body=UpdateUserSerializer,
        responses={
            200: ReadUserSerializer()
        }
    )
    def patch(request, user_id=None):
        logger.info(f"authenticated: {request.user}")
        user = get_user_by_id(user_id)
        if user is None:
            raise Http404
        user_serializer = UpdateUserSerializer(
            data=request.data,
            partial=True
        )
        user_serializer.is_valid(raise_exception=True)
        user = update_user(
            user,
            user_serializer.validated_data.get('username', user.username),
            user_serializer.validated_data.get('first_name', user.first_name),
            user_serializer.validated_data.get('last_name', user.last_name),
            user_serializer.validated_data.get('email', user.email),
            user_serializer.validated_data.get('password', user.password)
        )
        # NOTE: Re-serialize to fetch more detailed data
        user_serializer = ReadUserSerializer(user)
        return Response(user_serializer.data)

