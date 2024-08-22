from rest_framework import status, permissions
from rest_framework.response import Response
from rest_framework.views import APIView

from django.http import FileResponse

from user_management.models import User

class UserProfilePictureView(APIView):
     def get(self, request, pk):
          try:
               user = User.objects.get(pk=pk)
               response = FileResponse(user.photo_url)

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
               response['Content-Disposition'] = 'attachment; filename="'+user.username+'_photo.png"'
               return response
          except User.DoesNotExist:
               return Response({'error': 'SuratMasuk tidak ditemukan.'}, status=status.HTTP_404_NOT_FOUND)