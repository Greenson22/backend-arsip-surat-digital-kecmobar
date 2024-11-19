from rest_framework import viewsets, mixins
from ..models import IncomingLetter
from ..serializers import IncomingLetterSerializer

class IncomingLetterViewSet(viewsets.GenericViewSet, 
                            mixins.ListModelMixin,
                            mixins.CreateModelMixin,
                            mixins.RetrieveModelMixin,
                            mixins.UpdateModelMixin,
                            mixins.DestroyModelMixin):
     
     queryset = IncomingLetter.objects.all()
     serializer_class = IncomingLetterSerializer
     search_fields = ['source', 'recipient', 'agenda_number', 'letter_number', 'agenda_number', 'file', 'subject']