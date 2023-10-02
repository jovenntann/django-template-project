# DRF
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.pagination import PageNumberPagination
# from rest_framework.generics import ListAPIView

# Serializers
from .serializers import ReadProductSerializer, \
    CreateProductSerializer, PaginateReadProductSerializer, \
    PaginateQueryReadProductSerializer

# Services
from domain.products.services.service_Product import get_products, create_product

# Library: drf-yasg
from drf_yasg.utils import swagger_auto_schema

import json
import logging
logger = logging.getLogger(__name__)


# TODO: User Permission (Cause this section might only useful for Administrator or Moderator)

# NOTE: This is how to Paginate using limit and offset
# class ProductsAPIView(ListAPIView, PageNumberPagination, APIView):
#
#     permission_classes = (IsAuthenticated,)
#
#     queryset = Product.objects.all()
#     serializer_class = ReadProductSerializer

# NOTE: This is how to Paginate without using the ListAPIView
class ProductsAPIView(APIView):

    permission_classes = (IsAuthenticated,)

    @staticmethod
    @swagger_auto_schema(
        responses={
            200: PaginateReadProductSerializer()
        },
        operation_id="products_list",
        tags=["product-management.product"],
        query_serializer=PaginateQueryReadProductSerializer()
    )
    def get(request):
        logger.info(f"authenticated: {request.user}")
        # Optimization: this will query the database using IN list of categories
        products = get_products()
        paginator = PageNumberPagination()
        # paginator.page_size = 10
        result_page = paginator.paginate_queryset(products, request)
        product_serializer = ReadProductSerializer(result_page, many=True)
        # logger.info("response: %s", json.dumps(product_serializer.data, indent=4))
        return paginator.get_paginated_response(product_serializer.data)

    @staticmethod
    @swagger_auto_schema(
        request_body=CreateProductSerializer,
        operation_description="description",
        operation_id="products_create",
        tags=["product-management.product"],
        responses={
            200: ReadProductSerializer()
        }
    )
    def post(request, pk=None, *args, **kwargs):
        logger.info(f"authenticated: {request.user}")
        product_serializer = CreateProductSerializer(data=request.data)
        product_serializer.is_valid(raise_exception=True)
        product = create_product(
            product_serializer.validated_data['store'],
            product_serializer.validated_data.get('categories', []),
            product_serializer.validated_data['title'],
            product_serializer.validated_data['description'],
        )
        # NOTE: Re-serialize to fetch more detailed data
        product_serializer = ReadProductSerializer(product)
        # logger.info("response: %s", json.dumps(product_serializer.data, indent=4))
        return Response(product_serializer.data)
