from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model = User
		fields = ['id', 'username', 'password', 'first_name', 'last_name', 
		'email', 'is_active', 'is_superuser', 'date_joined', 'phone_number', 'photo_url']
		extra_kwargs = {'password': {'write_only': True}}
	
	def create(self, validated_data):
		user = User.objects.create(**validated_data)
		user.set_password(validated_data['password'])
		user.save()
		return user