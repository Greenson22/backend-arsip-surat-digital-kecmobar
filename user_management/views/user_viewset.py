from rest_framework import viewsets
from ..models import User
from ..serializers import UserSerializer
from .model_mixin import ListCustom, CreateCustom, RetrieveCustom, UpdateCustom, DestroyCustom

class UserViewSet(viewsets.GenericViewSet,
                  ListCustom,
                  CreateCustom,
                  RetrieveCustom,
                  UpdateCustom,
                  DestroyCustom):
     
    queryset = User.objects.all()
    serializer_class = UserSerializer
    search_fields = ['username', 'first_name', 'last_name', 'email', 'phone_number']

