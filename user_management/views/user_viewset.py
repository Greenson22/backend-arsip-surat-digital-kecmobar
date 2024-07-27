from rest_framework import viewsets, filters, status
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination

from django.http import Http404

from user_management.models import User
from user_management.serializers import UserSerializer

class StandardResultsSetPagination(PageNumberPagination):
    page_size = 5
    page_size_query_param = 'page_size'

class UserViewSet(viewsets.ViewSet):
    filter_backends = [filters.SearchFilter]
    pagination_class = StandardResultsSetPagination
    queryset = User.objects.all()
    search_fields = ['username', 'first_name', 'last_name', 'email', 'phone_number']

    def list(self, request, format=None):
        filtered_queryset = filters.SearchFilter().filter_queryset(self.request, self.queryset, self)
        paginator = self.pagination_class()
        paged_queryset = paginator.paginate_queryset(filtered_queryset, request)
        
        if paged_queryset is not None:
            serializer = UserSerializer(paged_queryset, many=True)
            return paginator.get_paginated_response(serializer.data)
        else:
            serializer = UserSerializer(self.queryset, many=True)
            return Response(serializer.data)

    def retrieve(self, request, pk):
        item = self.get_object(pk=pk)
        serializer = UserSerializer(item)
        return Response(serializer.data)

    def update(self, request, pk):
        item = self.get_object(pk)
        serializer = UserSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk):
        try:
            item = self.get_object(pk)
            item.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Http404:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def get_object(self, pk):
        try:
            return User.objects.get(pk=pk)
        except User.DoesNotExist:
            raise Http404