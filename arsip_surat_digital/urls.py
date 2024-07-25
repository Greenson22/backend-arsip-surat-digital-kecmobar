from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
    path('incoming_mail/', include('incoming_mail.urls')),
    path('users/', include('user_management.urls')),
]

urlpatterns += [
    path('api-auth/', include('rest_framework.urls')),
]

urlpatterns += [
     path('api-token-auth/', views.obtain_auth_token)
]