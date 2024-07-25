from rest_framework import serializers
from .models import IncomingLetter

class IncomingLetterSerializer(serializers.ModelSerializer):
    class Meta:
        model = IncomingLetter
        fields = '__all__'