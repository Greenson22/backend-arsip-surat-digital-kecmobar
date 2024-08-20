from rest_framework.serializers import ModelSerializer
from .models import OutgoingLetter

class OutgoingLetterSerializer(ModelSerializer):
     class Meta:
          model = OutgoingLetter
          fields = '__all__'