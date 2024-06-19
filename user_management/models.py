from django.db import models
from django.contrib.auth.models import AbstractUser

from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

class User(AbstractUser):
	phone_number = models.CharField(max_length=20, blank=True)  # Untuk nomor telepon
	photo_url = models.URLField(blank=True)  # Untuk URL foto

	def __str__(self):
		return self.phone_number

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)