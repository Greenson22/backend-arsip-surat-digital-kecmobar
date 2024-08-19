from rest_framework import generics, permissions
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.authentication import JWTAuthentication # type: ignore

from user_management.models import User
from user_management.serializers import UserSerializer

class UserCreateView(generics.CreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]