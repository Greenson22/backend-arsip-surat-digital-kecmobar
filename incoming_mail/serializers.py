from rest_framework import serializers
from .models import IncomingLetter

class IncomingLetterSerializer(serializers.ModelSerializer):
    class Meta:
        model = IncomingLetter
        fields = '__all__'

    # def get_file_url(self, obj):
    #     if obj.file:
    #         return obj.file.url
    #     return None