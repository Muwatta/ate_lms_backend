from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from .views import MeView, RegisterView

urlpatterns = [
    # Registration
    path('register/', RegisterView.as_view(), name='user-register'),

    # JWT login / refresh
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    # Get current user info
    path('me/', MeView.as_view(), name='user-me'),
]
