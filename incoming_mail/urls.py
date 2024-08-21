from django.urls import path
from rest_framework.routers import DefaultRouter
from incoming_mail.views import IncomingLetterFileView, IncomingLetterViewSet

router = DefaultRouter()
router.register('', IncomingLetterViewSet)

urlpatterns = [
    path('<int:pk>/file/', IncomingLetterFileView.as_view(), name='incoming-letter-file'),
]
urlpatterns += router.urls