from rest_framework import viewsets, permissions, authentication
from .models import User
from .serializers import UserSerializer

class UserViewSet(viewsets.ModelViewSet):
     queryset = User.objects.all()
     serializer_class = UserSerializer
     authentication_classes = [authentication.TokenAuthentication]
     permission_classes = [permissions.IsAuthenticated]