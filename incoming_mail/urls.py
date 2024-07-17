from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from incoming_mail.views import IncomingLetterListView, IncomingLetterDetailView, IncomingLetterFileView

urlpatterns = [
    path('', IncomingLetterListView.as_view()),
    path('<int:pk>/', IncomingLetterDetailView.as_view()),
    path('<int:pk>/file/', IncomingLetterFileView.as_view(), name='incoming-letter-file'),
]

urlpatterns = format_suffix_patterns(urlpatterns)