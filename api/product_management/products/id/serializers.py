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
