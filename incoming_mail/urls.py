from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path('', views.IncomingLetterList.as_view()),
    path('<int:pk>/', views.IncomingLetterDetail.as_view()),
    path('<int:pk>/file/', views.IncomingLetterFileView.as_view(), name='incoming-letter-file'),
]

urlpatterns = format_suffix_patterns(urlpatterns)