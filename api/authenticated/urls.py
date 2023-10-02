from django.urls import path
from .user.views import UserAPIView
from .user.profile.views import UserProfileAPIView
from .profile.views import ProfileAPIView


urlpatterns = [
    path('user', UserAPIView.as_view()),
    path('user/profile', UserProfileAPIView.as_view()),
    path('profile', ProfileAPIView.as_view())
]

