from django.db import models
from django.contrib.auth.models import AbstractUser

from django.dispatch import receiver
from rest_framework.authtoken.models import Token

class User(AbstractUser):
	phone_number = models.CharField(max_length=20, blank=True)  # Untuk nomor telepon
	photo_url = models.FileField(upload_to='profile', blank=True)

	def __str__(self):
		return self.phone_number