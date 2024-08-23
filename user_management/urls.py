from django.urls import include, path
from rest_framework import routers
from user_management.views import UserViewSet, UserProfilePictureView, UserPasswordViewSet

router = routers.DefaultRouter()
router.register('', UserViewSet, basename='user')
router.register('password', UserPasswordViewSet, basename='user-password')

urlpatterns = [
     path('<int:pk>/profile_picture/', UserProfilePictureView.as_view())
]

urlpatterns += router.urls