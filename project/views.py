from rest_framework.response import Response
from rest_framework.decorators import api_view

# Library: drf-yasg
from drf_yasg.utils import swagger_auto_schema

from .serializers import HealthCheckSerializer

import logging
logger = logging.getLogger(__name__)


@swagger_auto_schema(
    method='get',
    operation_id="health_check",
    responses={
        200: HealthCheckSerializer()
    }
)
@api_view(['GET'])
def health_check_view(request):
    logger.info(f"authenticated: {request.user}")
    content = {
        "status_code": 200,
        "status": "OK",
    }
    return Response(content)
