from django.urls import path
from rest_framework import routers

from .views import UserViewSet, UserProfilePictureView

router = routers.DefaultRouter()
router.register('', UserViewSet, basename='user')

urlpatterns = [
     path('<int:pk>/profile_picture/', UserProfilePictureView.as_view())
]

urlpatterns += router.urls