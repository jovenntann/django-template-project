from rest_framework import serializers

import logging
logger = logging.getLogger(__name__)


class HealthCheckSerializer(serializers.Serializer): # noqa

    status_code = serializers.IntegerField()
    status = serializers.CharField(max_length=100)

