from django.urls import path
from genai.views import ExtractLetterEntitiesView, SummarizeLetterView

urlpatterns = [
     path('extract_letter_entities/', ExtractLetterEntitiesView.as_view()), 
     path('summarize_letter/', SummarizeLetterView.as_view())
]