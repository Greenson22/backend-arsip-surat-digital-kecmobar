from rest_framework.views import APIView
from rest_framework import authentication, permissions, status
from rest_framework.response import Response

from django.http import FileResponse

from incoming_mail.models import IncomingLetter

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