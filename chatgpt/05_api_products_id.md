---
#### api/product_management/urls.py
```
from django.urls import path
from .products.views import ProductsAPIView
from .products.id.views import ProductsIdAPIView

urlpatterns = [
    path('products', ProductsAPIView.as_view()),
    path('products/<int:product_id>', ProductsIdAPIView.as_view()),
]
```

#### api/product_management/products/id/views.py
```
# DRF
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated

# Serializers
from .serializers import ReadProductSerializer, \
    UpdateProductSerializer, DeleteProductSerializer

# Services
from domain.products.services.service_Product import get_product_by_id, delete_product, \
    update_product

# Django Shortcuts
from django.shortcuts import get_object_or_404
from django.http import Http404

# Library: drf-yasg
from drf_yasg.utils import swagger_auto_schema

import logging
logger = logging.getLogger(__name__)


# TODO: User Permission (Cause this section might only useful for Administrator or Moderator)

class ProductsIdAPIView(APIView):

    permission_classes = (IsAuthenticated,)

    @staticmethod
    @swagger_auto_schema(
        responses={
            200: ReadProductSerializer()
        },
        operation_description="description",
        operation_id="products_read",
        tags=["product-management.product"],
    )
    def get(request, product_id=None):
        logger.info(f"authenticated: {request.user}")
        product = get_product_by_id(product_id)
        if product is None:
            raise Http404
        product_serializer = ReadProductSerializer(product)
        return Response(product_serializer.data)

    @staticmethod
    @swagger_auto_schema(
        operation_description="description",
        operation_id="products_delete",
        tags=["product-management.product"],
        responses={
            200: DeleteProductSerializer()
        }
    )
    def delete(request, product_id=None):
        logger.info(f"authenticated: {request.user}")
        product = get_product_by_id(product_id)
        if product is None:
            raise Http404
        # Copy product so that we can return this data from our delete response
        response = {
            'operation': 'delete',
            'domain': 'products',
            'model': 'Product',
            'data': product
        }
        response_serializer = DeleteProductSerializer(response)
        response_serializer_data = response_serializer.data

        delete_product(product)

        return Response(response_serializer_data)

    @staticmethod
    @swagger_auto_schema(
        operation_description="description",
        operation_id="products_update",
        tags=["product-management.product"],
        request_body=UpdateProductSerializer,
        responses={
            200: ReadProductSerializer()
        }
    )
    def put(request, product_id=None):
        logger.info(f"authenticated: {request.user}")

        product = get_product_by_id(product_id)

        if product is None:
            raise Http404

        product_serializer = UpdateProductSerializer(
            data=request.data
        )

        product_serializer.is_valid(raise_exception=True)

        update_product(
            product,
            product_serializer.validated_data.get('store', product.store),
            product_serializer.validated_data.get('categories', product.categories),
            product_serializer.validated_data.get('title', product.title),
            product_serializer.validated_data.get('description', product.description)
        )
        # NOTE: Re-serialize to fetch more detailed data
        product_serializer = ReadProductSerializer(
            product
        )
        return Response(product_serializer.data)

    @staticmethod
    @swagger_auto_schema(
        operation_description="description",
        operation_id="products_patch",
        tags=["product-management.product"],
        request_body=UpdateProductSerializer,
        responses={
            200: ReadProductSerializer()
        }
    )
    def patch(request, product_id=None):
        logger.info(f"authenticated: {request.user}")

        product = get_product_by_id(product_id)
        if product is None:
            raise Http404

        product_serializer = UpdateProductSerializer(
            data=request.data,
            partial=True
        )
        product_serializer.is_valid(raise_exception=True)

        update_product(
            product,
            product_serializer.validated_data.get('store', product.store),
            product_serializer.validated_data.get('categories', product.categories),
            product_serializer.validated_data.get('title', product.title),
            product_serializer.validated_data.get('description', product.description)
        )
        # NOTE: Re-serialize to fetch more detailed data
        product_serializer = ReadProductSerializer(
            product
        )
        return Response(product_serializer.data)
```

#### api/product_management/products/id/serializers.py
```
from rest_framework import serializers

# Models
from domain.products.models import Product, Category

import logging
logger = logging.getLogger(__name__)


class ReadCategorySerializer(serializers.ModelSerializer):

    class Meta:
        ref_name = "product_management.products.id.ReadCategorySerializer"
        model = Category
        fields = [
            'id',
            'name',
            'description',
            'created_at',
            'updated_at'
        ]


class ReadProductSerializer(serializers.ModelSerializer):

    categories = ReadCategorySerializer(many=True)

    class Meta:
        ref_name = "product_management.products.id.ReadProductSerializer"
        model = Product
        fields = [
            'id',
            'store',
            'categories',
            'title',
            'description',
            'created_at',
            'updated_at'
        ]


class UpdateProductSerializer(serializers.ModelSerializer):

    class Meta:
        ref_name = "product_management.products.id.UpdateProductSerializer"
        model = Product
        fields = [
            'store',
            'categories',
            'title',
            'description'
        ]


class DeleteProductSerializer(serializers.Serializer): # noqa

    class Meta:
        ref_name = "product_management.products.id.DeleteProductSerializer"

    operation = serializers.CharField(max_length=100)
    domain = serializers.CharField(max_length=200)
    model = serializers.CharField(max_length=100)
    data = ReadProductSerializer()
```
