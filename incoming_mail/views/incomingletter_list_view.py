from rest_framework.views import APIView
from rest_framework import authentication, permissions, filters, status
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response

from incoming_mail.models import IncomingLetter
from incoming_mail.serializers import IncomingLetterSerializer

class StandardResultsSetPagination(PageNumberPagination):
    page_size = 5
    page_size_query_param = 'page_size'

class IncomingLetterListView(APIView):
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