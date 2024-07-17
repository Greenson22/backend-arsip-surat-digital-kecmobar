from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView # type: ignore

urlpatterns = [
     path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair')
]