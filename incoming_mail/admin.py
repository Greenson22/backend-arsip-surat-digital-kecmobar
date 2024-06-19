from django.contrib import admin
from .models import Recipient, Source, IncomingLetter

# Register your models here.
admin.site.register(Recipient)
admin.site.register(Source)
admin.site.register(IncomingLetter)