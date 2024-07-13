from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken import views
from user_management.views import LoginView

urlpatterns = [
    path('api/login/', LoginView.as_view(), name='login'),
    path('admin/', admin.site.urls),
    path('incoming_mail/', include('incoming_mail.urls')),
    path('user_management/', include('user_management.urls')),
]

urlpatterns += [
    path('api-auth/', include('rest_framework.urls')),
]

urlpatterns += [
     path('api-token-auth/', views.obtain_auth_token)
]