# DRF
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated

# Serializers
from .serializers import ReadUserSerializer

# Library: drf-yasg more details at https://drf-yasg.readthedocs.io/en/stable/custom_spec.html
from drf_yasg.utils import swagger_auto_schema

import logging
logger = logging.getLogger(__name__)


class UserAPIView(APIView):

    permission_classes = (IsAuthenticated,)

    @staticmethod
    # Library: drf-yasg
    @swagger_auto_schema(
        responses={
            200: ReadUserSerializer()
        },
        operation_description="Read Authenticated User",
        operation_id="user_read"
    )
    def get(request):
        logger.info(f"authenticated: {request.user}")
        user_serializer = ReadUserSerializer(request.user)
        return Response(user_serializer.data)
