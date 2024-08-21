from django.urls import include, path
from rest_framework import routers
from user_management.views import UserViewSet, UserCreateView, UserProfilePictureView

router = routers.DefaultRouter()
router.register('', UserViewSet)

urlpatterns = [
     path('create/', UserCreateView.as_view()),
     path('user/<int:pk>/profile_picture/', UserProfilePictureView.as_view())
]

urlpatterns += router.urls