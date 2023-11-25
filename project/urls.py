"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path, include

from .views import health_check_view

# Library: drf-yasg
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

# Library: drf-yasg
schema_view = get_schema_view(
   openapi.Info(
      title="Snippets API",
      default_version='v1',
      description="Test description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
   url='https://api.tappy.com.ph/',
)


urlpatterns = [
    path('admin/', admin.site.urls),

    # Route to API's
    path('authentication/', include('api.authentication.urls')),
    path('authenticated/', include('api.authenticated.urls')),
    path('user-management/', include('api.user_management.urls')),
    path('store-management/', include('api.store_management.urls')),
    path('product-management/', include('api.product_management.urls')),
    path('health-check', health_check_view),

    # Library: drf-yasg
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    re_path(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
