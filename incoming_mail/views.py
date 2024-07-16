from rest_framework import status, authentication, permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import Http404
from .models import IncomingLetter
from .serializers import IncomingLetterSerializer
from rest_framework.pagination import PageNumberPagination
from rest_framework import filters
from django.http import FileResponse


class StandardResultsSetPagination(PageNumberPagination):
    page_size = 5
    page_size_query_param = 'page_size'

class IncomingLetterList(APIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    
    filter_backends = [filters.SearchFilter]
    search_fields = ['id', 'source', 'recipient', 'agenda_number', 'letter_number', 'agenda_number', 'letter_date', 'received_date', 'file', 'subject']
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
            validated_data = serializer.validated_data
            # Handle file upload
            file = request.FILES.get('file')
            new_filename = validated_data['letter_number'].replace('/','_')+' '+validated_data['letter_number'].replace('/', '_')+'.pdf'
            
            # Create the IncomingLetter instance
            incoming_letter = IncomingLetter(
                source=validated_data['source'],
                recipient=validated_data['recipient'],
                letter_number=validated_data['letter_number'],
                agenda_number=validated_data['agenda_number'],
                letter_date=validated_data['letter_date'],
                received_date=validated_data['received_date'],
                file=file,
                subject=validated_data['subject']
            )

            incoming_letter.file.name = new_filename
            incoming_letter.save()
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
        incoming_letter.file
        return Response(status=status.HTTP_204_NO_CONTENT)

class IncomingLetterFileView(APIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, pk, format=None):
        try:
            incoming_letter = IncomingLetter.objects.get(pk=pk)
            response = FileResponse(incoming_letter.file, content_type='application/pdf')

            # Menambahkan CSP Header
            csp_string = (
                "default-src 'none'; "  # Default tidak mengizinkan apa pun
                "frame-ancestors http://localhost:5173/; "  # 
                "form-action 'self'; "  # Form hanya boleh di-submit ke domain yang sama
                "base-uri 'self'; "  # Base URI harus sama dengan domain saat ini
                "object-src 'none'; "  # Tidak boleh memuat objek (Flash, dll.)
                "img-src 'self'; "  # Hanya boleh memuat gambar dari domain yang sama
                "script-src 'none'; "  # Tidak boleh menjalankan JavaScript
                "style-src 'self'; "  # Hanya boleh memuat gaya dari domain yang sama
                "connect-src 'self'; "  # Hanya boleh terhubung ke domain yang sama
                "report-uri /csp-report;"  # URL untuk pelaporan pelanggaran (opsional)
            )
            response["Content-Security-Policy"] = csp_string
            return response
        except IncomingLetter.DoesNotExist:
            return Response({'error': 'SuratMasuk tidak ditemukan.'}, status=status.HTTP_404_NOT_FOUND)