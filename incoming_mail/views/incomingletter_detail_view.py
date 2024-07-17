from rest_framework.views import APIView
from rest_framework import authentication, permissions, status
from rest_framework.response import Response

from django.http import Http404

from incoming_mail.models import IncomingLetter
from incoming_mail.serializers import IncomingLetterSerializer

class IncomingLetterDetailView(APIView):
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