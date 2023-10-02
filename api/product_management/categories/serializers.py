from rest_framework import serializers

# Models
from domain.products.models import Category

import logging
logger = logging.getLogger(__name__)


class ReadCategorySerializer(serializers.ModelSerializer):
    class Meta:
        ref_name = "product_management.categories.ReadCategorySerializer"
        model = Category
        fields = [
            'id',
            'name',
            'description',
            'created_at',
            'updated_at'
        ]


class CreateCategorySerializer(serializers.ModelSerializer):
    class Meta:
        ref_name = "product_management.categories.CreateCategorySerializer"
        model = Category
        fields = [
            'name',
            'description'
        ]


class PaginateReadCategorySerializer(serializers.Serializer): # noqa

    class Meta:
        ref_name = "product_management.categories.PaginateReadCategorySerializer"

    count = serializers.IntegerField()
    next = serializers.URLField()
    previous = serializers.URLField()
    results = ReadCategorySerializer(many=True)

class PaginateQueryReadCategorySerializer(serializers.Serializer): # noqa

    class Meta:
        ref_name = "product_management.categories.PaginateQueryReadCategorySerializer"

    page = serializers.IntegerField(required=False, help_text="A page number within the paginated result set.")
