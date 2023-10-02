# DRF
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated

# Django Shortcuts
from django.http import Http404

# Serializers
from .serializers import ReadCategorySerializer, \
    DeleteCategorySerializer, UpdateCategorySerializer

# Services
from domain.products.services.service_Category import get_category_by_id, delete_category, \
    update_category

from drf_yasg.utils import swagger_auto_schema

import logging
logger = logging.getLogger(__name__)


class CategoriesIdAPIView(APIView):

    permission_classes = (IsAuthenticated,)

    @staticmethod
    @swagger_auto_schema(
        operation_id="categories_read",
        tags=["product-management.category"],
        responses={
            200: ReadCategorySerializer()
        },
    )
    def get(request, category_id=None):
        logger.info(f"authenticated: {request.user}")
        category = get_category_by_id(category_id)
        if category is None:
            raise Http404
        category_serializer = ReadCategorySerializer(category)
        return Response(category_serializer.data)

    @staticmethod
    @swagger_auto_schema(
        operation_description="description",
        operation_id="categories_delete",
        tags=["product-management.category"],
        responses={
            200: DeleteCategorySerializer()
        }
    )
    def delete(request, category_id=None):
        logger.info(f"authenticated: {request.user}")
        category = get_category_by_id(category_id)
        if category is None:
            raise Http404
        # Copy category so that we can return this data from our delete response
        response = {
            'operation': 'delete',
            'domain': 'products',
            'model': 'Category',
            'data': category
        }
        response_serializer = DeleteCategorySerializer(response)
        response_serializer_data = response_serializer.data

        delete_category(category)

        return Response(response_serializer_data)

    @staticmethod
    @swagger_auto_schema(
        operation_description="description",
        operation_id="categories_update",
        tags=["product-management.category"],
        request_body=UpdateCategorySerializer,
        responses={
            200: ReadCategorySerializer()
        }
    )
    def put(request, category_id=None):
        logger.info(f"authenticated: {request.user}")

        category = get_category_by_id(category_id)
        if category is None:
            raise Http404

        category_serializer = UpdateCategorySerializer(
            data=request.data
        )

        category_serializer.is_valid(raise_exception=True)
        update_category(
            category,
            category_serializer.validated_data.get('name', category.name),
            category_serializer.validated_data.get('description', category.description),
        )
        category_serializer = ReadCategorySerializer(
            category
        )
        return Response(category_serializer.data)

    @staticmethod
    @swagger_auto_schema(
        operation_description="description",
        operation_id="categories_patch",
        tags=["product-management.category"],
        request_body=ReadCategorySerializer,
        responses={
            200: UpdateCategorySerializer()
        }
    )
    def patch(request, category_id=None):
        logger.info(f"authenticated: {request.user}")
        category = get_category_by_id(category_id)

        if category is None:
            raise Http404

        category_serializer = UpdateCategorySerializer(
            data=request.data,
            partial=True
        )
        category_serializer.is_valid(raise_exception=True)

        update_category(
            category,
            category_serializer.validated_data.get('name', category.name),
            category_serializer.validated_data.get('description', category.description),
        )
        category_serializer = ReadCategorySerializer(
            category
        )
        return Response(category_serializer.data)
