# DRF
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated

# Serializers
from .serializers import ReadProfileSerializer

# Models
from domain.users.models import Profile

# Django: https://docs.djangoproject.com/en/4.1/topics/http/shortcuts/
from django.shortcuts import get_object_or_404

# Library: drf-yasg more details at https://drf-yasg.readthedocs.io/en/stable/custom_spec.html
from drf_yasg.utils import swagger_auto_schema

import logging
logger = logging.getLogger(__name__)


class ProfileAPIView(APIView):

    permission_classes = (IsAuthenticated,)

    @staticmethod
    @swagger_auto_schema(
        responses={
            200: ReadProfileSerializer()
        },
        operation_description="Read Authenticated User Profile",
        operation_id="profile_read"
    )
    def get(request):
        logger.info(f"authenticated: {request.user}")
        profile = get_object_or_404(Profile, user=request.user)
        profile_serializer = ReadProfileSerializer(profile)
        return Response(profile_serializer.data)
