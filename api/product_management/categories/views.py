# DRF
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.pagination import PageNumberPagination

# Serializers
from .serializers import ReadCategorySerializer, CreateCategorySerializer, \
    PaginateQueryReadCategorySerializer, PaginateReadCategorySerializer

# Services
from domain.products.services.service_Category import get_categories, create_category

from drf_yasg.utils import swagger_auto_schema

import logging
logger = logging.getLogger(__name__)


class CategoriesAPIView(APIView):

    permission_classes = (IsAuthenticated,)

    @staticmethod
    @swagger_auto_schema(
        responses={
            200: PaginateReadCategorySerializer()
        },
        operation_id="categories_list",
        query_serializer=PaginateQueryReadCategorySerializer(),
        tags=["product-management.category"],
    )
    def get(request):
        logger.info(f"authenticated: {request.user}")
        categories = get_categories()
        paginator = PageNumberPagination()
        result_page = paginator.paginate_queryset(categories, request)
        product_serializer = ReadCategorySerializer(result_page, many=True)
        return paginator.get_paginated_response(product_serializer.data)

    @staticmethod
    @swagger_auto_schema(
        request_body=CreateCategorySerializer,
        operation_description="description",
        operation_id="categories_create",
        tags=["product-management.category"],
        responses={
            200: ReadCategorySerializer()
        }
    )
    def post(request, pk=None, *args, **kwargs):
        logger.info(f"authenticated: {request.user}")
        category_serializer = CreateCategorySerializer(data=request.data)
        category_serializer.is_valid(raise_exception=True)
        category = create_category(
            category_serializer.validated_data.get('name'),
            category_serializer.validated_data.get('description'),
        )
        category_serializer = ReadCategorySerializer(category)
        return Response(category_serializer.data)
