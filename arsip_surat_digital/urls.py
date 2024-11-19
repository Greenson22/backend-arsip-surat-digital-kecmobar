from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
    path('genai/', include('genai.urls')),
    path('incoming_mail/', include('incoming_mail.urls')),
    path('outgoing_mail/', include('outgoing_mail.urls')),
    path('users/', include('user_management.urls')),
    path('api-auth/', include('rest_framework.urls')),
    path('api-token-auth/', views.obtain_auth_token),
]