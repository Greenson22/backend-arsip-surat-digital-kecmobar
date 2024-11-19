from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import FileResponse

from ..models import OutgoingLetter


class OutgoingLetterFileView(APIView):
     def get(self, request, pk, format=None):
          try:
               letter = OutgoingLetter.objects.get(pk=pk)
               response = FileResponse(letter.file, content_type='application/pdf')

               # Menambahkan CSP Header
               csp_string = (
                    "default-src 'none'; "  # Default tidak mengizinkan apa pun
                    "frame-ancestors http://localhost:5173/; "
                    "form-action 'self'; "  # Form hanya boleh di-submit ke domain yang sama
                    "base-uri 'self'; "  # Base URI harus sama dengan domain saat ini
                    "object-src 'none'; "  # Tidak boleh memuat objek (Flash, dll.)
                    "img-src 'self'; "  # Hanya boleh memuat gambar dari domain yang sama
                    "script-src 'none'; "  # Tidak boleh menjalankan JavaScript
                    "style-src 'self'; "  # Hanya boleh memuat gaya dari domain yang sama
                    "connect-src 'self'; "  # Hanya boleh terhubung ke domain yang sama
                    "report-to /csp-report;"  # URL untuk pelaporan pelanggaran (opsional)
               )

               response["Content-Security-Policy"] = csp_string
               response['Content-Disposition'] = 'attachment; filename="document.pdf"'
               return response
          except OutgoingLetter.DoesNotExist:
               return Response({'detail: Surat keluar tidak ditemukan.'}, status=status.HTTP_404_NOT_FOUND)