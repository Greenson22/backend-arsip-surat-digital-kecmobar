from django.urls import path
from genai.views import ExtractLetterEntitiesView, SummarizeLetterView, LetterOCRView, LetterClassificationView

urlpatterns = [
     path('extract_letter_entities/', ExtractLetterEntitiesView.as_view()),
     path('letter_ocr/', LetterOCRView.as_view()),
     path('letter_classification/', LetterClassificationView.as_view()), 
     path('summarize_letter/', SummarizeLetterView.as_view())
]