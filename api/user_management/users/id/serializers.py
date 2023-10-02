from rest_framework import serializers

# Models
from django.contrib.auth.models import User


class ReadUserSerializer(serializers.ModelSerializer):
    class Meta:
        ref_name = "user_management.users.id.ReadUserSerializer"
        model = User
        fields = [
            'id',
            'username',
            'first_name',
            'last_name',
            'email'
        ]


class UpdateUserSerializer(serializers.ModelSerializer):
    class Meta:
        ref_name = "user_management.users.id.UpdateUserSerializer"
        model = User
        fields = [
            'id',
            'username',
            'first_name',
            'last_name',
            'email',
            'password'
        ]


class DeleteUserSerializer(serializers.Serializer): # noqa

    class Meta:
        ref_name = "user_management.users.id.DeleteUserSerializer"

    operation = serializers.CharField(max_length=100)
    domain = serializers.CharField(max_length=200)
    model = serializers.CharField(max_length=100)
    data = ReadUserSerializer()
