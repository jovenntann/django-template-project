from rest_framework import serializers

# Models
from domain.stores.models import Store

import logging
logger = logging.getLogger(__name__)


class ReadStoreSerializer(serializers.ModelSerializer):
    class Meta:
        ref_name = "store_management.stores.id.ReadStoreSerializer"
        model = Store
        fields = [
            'id',
            'user',
            'name',
            'contact_number',
            'address',
            'created_at',
            'updated_at'
        ]


class DeleteStoreSerializer(serializers.Serializer): # noqa
    class Meta:
        ref_name = "store_management.stores.id.DeleteStoreSerializer"

    operation = serializers.CharField(max_length=100)
    domain = serializers.CharField(max_length=200)
    model = serializers.CharField(max_length=100)
    data = ReadStoreSerializer()


class UpdateStoreSerializer(serializers.ModelSerializer):

    class Meta:
        ref_name = "store_management.stores.id.UpdateStoreSerializer"
        model = Store
        fields = [
            'name',
            'contact_number',
            'address'
        ]
