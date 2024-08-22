from rest_framework import filters, status
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework.exceptions import PermissionDenied
from django.http import Http404

from ..models import IncomingLetter
from ..serializers import IncomingLetterSerializer
from arsip_surat_digital.views import StandardResultPagePagination


class IncomingLetterViewSet(ViewSet):
     pagination_class = StandardResultPagePagination
     queryset = IncomingLetter.objects.all()
     serializer = IncomingLetterSerializer
     search_fields = ['source', 'recipient', 'agenda_number', 'letter_number', 'agenda_number', 'file', 'subject']

     def list(self, request):
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
          serializer = self.serializer(letter, dat=request.data)
          if serializer.is_valid():
               serializer.save()
               return Response(serializer.data)
          return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

     def destroy(self, request, pk):
          try:
               letter = self.get_object(pk=pk)
               letter.delete()
               return Response({'detail':'Surat berhasil dihapus'},
                               status=status.HTTP_204_NO_CONTENT)
          except PermissionDenied:
               return Response({'detail':'Anda tidak memiliki izin untuk menghapus surat ini'}, 
                               status=status.HTTP_403_FORBIDDEN)
          except Exception as e:
               return Response({"detail": f"Terjadi kesalahan saat menghapus surat: {str(e)}"}, 
                               status=status.HTTP_500_INTERNAL_SERVER_ERROR)

     def get_object(self, pk):
          try:
               return IncomingLetter.objects.get(pk=pk)
          except IncomingLetter.DoesNotExist:
               raise Http404('Surat tidak ditemukan')