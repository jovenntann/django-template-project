from rest_framework import serializers

# Models
from domain.products.models import Category

import logging
logger = logging.getLogger(__name__)


class ReadCategorySerializer(serializers.ModelSerializer):
    class Meta:
        ref_name = "product_management.categories.id.ReadCategorySerializer"
        model = Category
        fields = [
            'id',
            'name',
            'description',
            'created_at',
            'updated_at'
        ]


class UpdateCategorySerializer(serializers.ModelSerializer): # noqa

    class Meta:
        ref_name = "product_management.categories.id.UpdateCategorySerializer"
        model = Category
        fields = [
            'id',
            'name',
            'description',
        ]


class DeleteCategorySerializer(serializers.Serializer): # noqa

    class Meta:
        ref_name = "product_management.categories.id.DeleteCategorySerializer"
        
    operation = serializers.CharField(max_length=100)
    domain = serializers.CharField(max_length=200)
    model = serializers.CharField(max_length=100)
    data = ReadCategorySerializer()
