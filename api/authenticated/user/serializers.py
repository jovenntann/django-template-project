from rest_framework import serializers

# Models
from domain.users.models import User


class ReadUserSerializer(serializers.ModelSerializer):
    class Meta:
        ref_name = "authenticated.user.ReadUserSerializer"
        model = User
        fields = [
            'id',
            'username',
            'first_name',
            'last_name',
            'email',
            'password'
        ]

        extra_kwargs = {
            'password': {'write_only': True}
        }

