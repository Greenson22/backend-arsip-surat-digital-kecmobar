from rest_framework.routers import DefaultRouter
from .views import OutgoingLetterViewSet

router = DefaultRouter()
router.register('', OutgoingLetterViewSet)

urlpatterns = router.urls