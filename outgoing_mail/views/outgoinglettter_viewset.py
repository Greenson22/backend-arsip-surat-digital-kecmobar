from rest_framework import viewsets, filters, status
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from rest_framework.exceptions import PermissionDenied

from django.http import Http404
from django.utils.text import slugify
import uuid

from ..models import OutgoingLetter
from ..serializer import OutgoingLetterSerializer

class StandarResultsSetPagination(PageNumberPagination):
     page_size = 5
     page_size_query_param = 'page_size'

class OutgoingLetterViewSet(viewsets.ViewSet):
     pagination_class = StandarResultsSetPagination
     queryset = OutgoingLetter.objects.all()
     pagination_class = StandarResultsSetPagination
     search_fields = ['agenda_number', 'letter_number', 'destination', 'subject']
     serializer = OutgoingLetterSerializer

     def list(self, request, format=None):
          filtered_querset = filters.SearchFilter().filter_queryset(self.request, self.queryset, self)
          paginator = self.pagination_class()
          page_queryset = paginator.paginate_queryset(filtered_querset, request)

          if page_queryset is not None:
               serializer = self.serializer(page_queryset, many=True)
               return paginator.get_paginated_response(serializer.data)
          else:
               serializer = self.serializer(self.queryset, many=True)
               return Response(serializer.data)

     def create(self, request):
          serializer = self.serializer(request.data)
          if serializer.is_valid():
               serializer.save()
               return Response(serializer.data, status=status.HTTP_201_CREATED)
          return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

     def retrieve(self, request, pk):
          letter = self.get_object(pk=pk)
          serializer = self.serializer(letter)
          return Response(serializer.data)
          
     def update(self, request, pk):
          letter = self.get_object(pk=pk)
          serializer = self.serializer(letter, data=request.data)
          if serializer.is_valid():
               serializer.save()
               return Response(serializer.data)
          return Response(serializer.erros, status=status.HTTP_400_BAD_REQUEST)
     
     def destroy(self, request, pk):
          try:
               letter = self.get_object(pk=pk)
               letter.delete()
               return Response({'detail':'object berhasil dihapus'}, 
                               status=status.HTTP_204_NO_CONTENT)
          except PermissionDenied:
               return Response({'detail':'anda tidak memiliki izin untuk menghapus object ini'}, 
                               status=status.HTTP_403_FORBIDDEN)
          except Exception as e:
               return Response({"detail": f"Terjadi kesalahan saat menghapus objek: {str(e)}"}, 
                               status=status.HTTP_500_INTERNAL_SERVER_ERROR)

     def get_object(self, pk):
          try:
               return OutgoingLetter.objects.get(pk=pk)
          except OutgoingLetter.DoesNotExist:
               return Http404

     def rename_file(self, request, name):
        # Handling Photo Upload
        if 'photo_url' in request.FILES:  # Periksa apakah ada foto yang diunggah
            photo = request.FILES['file']

            # Buat nama file baru
            ext = photo.name.split('.')[-1]  # Ambil ekstensi file asli
            new_filename = f"{slugify(name)}-{uuid.uuid4().hex[:6]}.{ext}"  # Nama file baru
            photo.name = new_filename