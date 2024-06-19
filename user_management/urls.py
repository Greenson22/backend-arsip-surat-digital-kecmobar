from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

user_list = views.UserViewSet.as_view({
     'get' : 'list',
     'post' : 'create',
})

user_detail = views.UserViewSet.as_view({
     'get' : 'retrieve',
     'put' : 'update',
     'delete' : 'destroy'
})

urlpatterns = [
    path('', user_list),
    path('<int:pk>', user_detail)
]

urlpatterns = format_suffix_patterns(urlpatterns)