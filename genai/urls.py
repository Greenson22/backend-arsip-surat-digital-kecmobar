from django.urls import path
from genai.views import LetterDetailView

urlpatterns = [
     path('letter_detail/', LetterDetailView.as_view())
]