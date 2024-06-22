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
    recipient = RecipientSerializer()  # Nested serializer
    source = SourceSerializer()      # Nested serializer

    class Meta:
        model = IncomingLetter
        fields = '__all__'

class IncomingLetterSerializerSelectedReleated(serializers.ModelSerializer):

    class Meta:
        model = IncomingLetter
        fields = '__all__'

class IncomingLetterSerializerPost(serializers.ModelSerializer):
    class Meta:
        model = IncomingLetter
        fields = [
            'id', 'letter_number', 'agenda_number', 'letter_date', 
            'received_date', 'recipient', 'source', 'file_url', 
            'subject', 'created_at', 'updated_at'
        ]