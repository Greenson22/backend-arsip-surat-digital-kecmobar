from django.urls import path
from django.http import HttpResponse

from . import views as blog_views

urlpatterns = [
	path('', blog_views.index),
]