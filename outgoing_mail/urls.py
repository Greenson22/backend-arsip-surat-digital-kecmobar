from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import OutgoingLetterViewSet, OutgoingLetterFileView

router = DefaultRouter()
router.register('', OutgoingLetterViewSet)

urlpatterns = [
     path('<int:pk>/file/', OutgoingLetterFileView.as_view(), name='outgoingletter-file')
]
urlpatterns += router.urls