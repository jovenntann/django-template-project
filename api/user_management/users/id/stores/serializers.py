from rest_framework import serializers

# Models
from domain.users.models import User
from domain.stores.models import Store


class ReadUserSerializer(serializers.ModelSerializer):
    class Meta:
        ref_name = "user_management.users.id.stores.ReadUserSerializer"
        model = User
        fields = [
            'id',
            'username',
            'first_name',
            'last_name',
            'email'
        ]


class ReadStoreSerializer(serializers.ModelSerializer):

    class Meta:
        ref_name = "user_management.users.id.stores_ReadStoreSerializer"
        model = Store
        fields = [
            'id',
            'name',
            'contact_number',
            'address',
            'created_at',
            'updated_at'
        ]


class ReadUserStoreSerializer(serializers.ModelSerializer):

    stores = ReadStoreSerializer(read_only=True, many=True)

    class Meta:
        ref_name = "user_management.users.id.stores.ReadUserProfileSerializer"
        model = User
        fields = [
            'id',
            'username',
            'first_name',
            'last_name',
            'email',
            'stores'
        ]
