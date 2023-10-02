# DRF
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated

# Serializers
from .serializers import ReadUserProfileSerializer

# Services
from domain.users.services.service_User import get_user_by_id

# Django Shortcuts
from django.http import Http404

# Library: drf-yasg
from drf_yasg.utils import swagger_auto_schema

import logging
logger = logging.getLogger(__name__)


# TODO: User Permission (Cause this section might only useful for Administrator or Moderator)

class UsersIdProfileAPIView(APIView):

    permission_classes = (IsAuthenticated,)

    @staticmethod
    @swagger_auto_schema(
        responses={
            200: ReadUserProfileSerializer()
        },
        operation_description="description",
        operation_id="users_profile_read.",
        tags=["user-management"],
    )
    def get(request, user_id=None):
        logger.info(f"authenticated: {request.user}")
        user = get_user_by_id(user_id)
        if user is None:
            raise Http404
        user_serializer = ReadUserProfileSerializer(user)
        return Response(user_serializer.data)

