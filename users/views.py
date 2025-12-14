from rest_framework import generics
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .serializers import UserRegisterSerializer

class RegisterView(generics.CreateAPIView):
    """
    Endpoint: POST /api/auth/register/
    Creates a new user.
    """
    serializer_class = UserRegisterSerializer


class MeView(generics.RetrieveAPIView):
    """
    Endpoint: GET /api/auth/me/
    Returns the current logged-in user's info.
    Requires JWT authentication.
    """
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        user = request.user
        return Response({
            "id": user.id,
            "username": user.username,
            "email": user.email,
            "role": user.role
        })
