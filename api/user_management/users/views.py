# DRF
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.pagination import PageNumberPagination

# Serializers
from .serializers import ReadUserSerializer, CreateUserSerializer, PaginateUserSerializer, \
    PaginateQueryUserSerializer

# Permission
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from domain.users.permissions.permission_group import IsAdminUser

# Services
from domain.users.services.service_User import get_users, create_user

# Library: drf-yasg
from drf_yasg.utils import swagger_auto_schema

import logging
logger = logging.getLogger(__name__)


class UsersAPIView(APIView):

    # Example of Class Based Permissions (We need to have specific permission as well)
    # permission_classes = [IsAdminUser, IsAdminOrAnonymousUser]
    permission_classes = [IsAdminUser]

    @staticmethod
    @swagger_auto_schema(
        responses={
            200: PaginateUserSerializer()
        },
        operation_id="users_list",
        tags=["user-management"],
        query_serializer=PaginateQueryUserSerializer()
    )
    def get(request):
        logger.info(f"authenticated: {request.user}")
        users = get_users()
        paginator = PageNumberPagination()
        result_page = paginator.paginate_queryset(users, request)
        # paginator.page_size = 10
        user_serializer = ReadUserSerializer(result_page, many=True)
        return paginator.get_paginated_response(user_serializer.data)

    @staticmethod
    @swagger_auto_schema(
        request_body=CreateUserSerializer,
        operation_description="description",
        operation_id="users_create",
        tags=["user-management"],
    )
    def post(request, pk=None, *args, **kwargs):
        logger.info(f"authenticated: {request.user}")
        user_serializer = CreateUserSerializer(data=request.data)
        user_serializer.is_valid(raise_exception=True)
        user = create_user(
            user_serializer.validated_data.get('username'),
            user_serializer.validated_data.get('first_name', ''),
            user_serializer.validated_data.get('last_name', ''),
            user_serializer.validated_data.get('email'),
            user_serializer.validated_data.get('password'),
        )
        logger.info(f"user created {user}")
        # NOTE: Re-serialize to fetch more detailed data
        user_serializer = ReadUserSerializer(user)
        return Response(user_serializer.data)
