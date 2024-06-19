from rest_framework import serializers
from .models import Recipient, Source, IncomingLetter

class RecipientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recipient
        fields = ['id', 'name'] 

class SourceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Source
        fields = ['id', 'name']

class IncomingLetterSerializer(serializers.ModelSerializer):
    recipient = RecipientSerializer(read_only=True)  # Nested serializer
    source = SourceSerializer(read_only=True)      # Nested serializer

    class Meta:
        model = IncomingLetter
        fields = [
            'id', 'letter_number', 'agenda_number', 'letter_date', 
            'received_date', 'recipient', 'source', 'file_url', 
            'subject', 'created_at', 'updated_at'
        ]
