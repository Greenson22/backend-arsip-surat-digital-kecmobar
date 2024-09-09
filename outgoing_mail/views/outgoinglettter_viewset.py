from rest_framework import viewsets, mixins
from ..models import OutgoingLetter
from ..serializer import OutgoingLetterSerializer

class OutgoingLetterViewSet(viewsets.GenericViewSet,
                            mixins.ListModelMixin,
                            mixins.CreateModelMixin,
                            mixins.RetrieveModelMixin,
                            mixins.UpdateModelMixin,
                            mixins.DestroyModelMixin):
     
     queryset = OutgoingLetter.objects.all()
     serializer_class = OutgoingLetterSerializer
     search_fields = ['agenda_number', 'letter_number', 'destination', 'subject']