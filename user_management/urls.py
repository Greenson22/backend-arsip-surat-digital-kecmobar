from django.urls import include, path
from rest_framework import routers
from user_management.views import UserViewSet, UserCreateView

router = routers.DefaultRouter()
router.register(r'user', UserViewSet)

urlpatterns = [
     path('', include(router.urls)),
     path('create/', UserCreateView.as_view())
]