# DRF
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated

# Serializers
from .serializers import ReadUserProfileSerializer

# Library: drf-yasg more details at https://drf-yasg.readthedocs.io/en/stable/custom_spec.html
from drf_yasg.utils import swagger_auto_schema

import logging
logger = logging.getLogger(__name__)


class UserProfileAPIView(APIView):

    permission_classes = (IsAuthenticated,)

    @staticmethod
    @swagger_auto_schema(
        responses={
            200: ReadUserProfileSerializer()
        },
        operation_description="Read Authenticated User Profile",
        operation_id="user_profile_read"
    )
    def get(request):
        logger.info(f"authenticated: {request.user}")
        user_serializer = ReadUserProfileSerializer(request.user)
        return Response(user_serializer.data)
