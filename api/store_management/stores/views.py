# DRF
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.pagination import PageNumberPagination

# Serializers
from .serializers import ReadStoreSerializer, CreateStoreSerializer, \
    PaginateQueryReadStoreSerializer, PaginateReadStoreSerializer

# Services
from domain.stores.services.service_Store import get_stores, create_store

from drf_yasg.utils import swagger_auto_schema

import logging
logger = logging.getLogger(__name__)


class StoresAPIView(APIView):

    permission_classes = (IsAuthenticated,)

    @staticmethod
    @swagger_auto_schema(
        responses={
            200: PaginateReadStoreSerializer()
        },
        operation_id="stores_list",
        query_serializer=PaginateQueryReadStoreSerializer(),
        tags=["store-management"],
    )
    def get(request):
        logger.info(f"authenticated: {request.user}")
        stores = get_stores()
        paginator = PageNumberPagination()
        result_page = paginator.paginate_queryset(stores, request)
        product_serializer = ReadStoreSerializer(result_page, many=True)
        return paginator.get_paginated_response(product_serializer.data)

    @staticmethod
    @swagger_auto_schema(
        request_body=CreateStoreSerializer,
        operation_description="description",
        operation_id="stores_create",
        tags=["store-management"],
        responses={
            200: ReadStoreSerializer()
        }
    )
    def post(request, pk=None, *args, **kwargs):
        logger.info(f"authenticated: {request.user}")
        store_serializer = CreateStoreSerializer(data=request.data)
        store_serializer.is_valid(raise_exception=True)
        store = create_store(
            request.user,
            store_serializer.validated_data.get('name'),
            store_serializer.validated_data.get('contact_number'),
            store_serializer.validated_data.get('address'),
        )
        store_serializer = ReadStoreSerializer(store)
        return Response(store_serializer.data)
