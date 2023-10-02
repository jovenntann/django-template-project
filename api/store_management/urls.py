from django.urls import path
from .stores.views import StoresAPIView
from .stores.id.views import StoresIdAPIView

urlpatterns = [
    path('stores', StoresAPIView.as_view()),
    path('stores/<int:store_id>', StoresIdAPIView.as_view()),
]
