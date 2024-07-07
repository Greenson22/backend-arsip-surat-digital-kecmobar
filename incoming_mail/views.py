from rest_framework import status, authentication, permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import Http404
from .models import IncomingLetter
from .serializers import IncomingLetterSerializer
from rest_framework.pagination import PageNumberPagination
from rest_framework import filters

class StandardResultsSetPagination(PageNumberPagination):
    page_size = 5
    page_size_query_param = 'page_size'

class IncomingLetterList(APIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [filters.SearchFilter]
    search_fields = ['id', 'source', 'recipient', 'agenda_number', 'letter_number', 
                     'agenda_number', 'letter_date', 'received_date', 'file_url', 'subject']
    pagination_class = StandardResultsSetPagination

    def get(self, request, format=None):
        queryset = IncomingLetter.objects.all()
        filtered_queryset = self.filter_queryset(queryset)
        paginator = self.pagination_class()
        paged_queryset = paginator.paginate_queryset(filtered_queryset, request)

        if paged_queryset is not None:
            serializer = IncomingLetterSerializer(paged_queryset, many=True)
            return paginator.get_paginated_response(serializer.data)
        else:
            serializer = IncomingLetterSerializer(queryset, many=True)
            return Response(serializer.data)

    def post(self, request, format=None):
        serializer = IncomingLetterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def filter_queryset(self, queryset):
        for backend in list(self.filter_backends):
            queryset = backend().filter_queryset(self.request, queryset, self)
        return queryset

class IncomingLetterDetail(APIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self, pk):
        try:
            return IncomingLetter.objects.get(pk=pk)
        except IncomingLetter.DoesNotExist:
            raise Http404
    
    def get(self, request, pk, format=None):
        incoming_letter = self.get_object(pk)
        serializer = IncomingLetterSerializer(incoming_letter)
        return Response(serializer.data)
    
    def put(self, request, pk, format=None):
        incoming_letter = self.get_object(pk=pk)
        serializer = IncomingLetterSerializer(incoming_letter, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        incoming_letter = self.get_object(pk)
        incoming_letter.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)