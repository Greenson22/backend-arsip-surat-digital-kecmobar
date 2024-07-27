from rest_framework import generics
from rest_framework.permissions import AllowAny

from user_management.models import User
from user_management.serializers import UserSerializer

class UserCreateView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]
