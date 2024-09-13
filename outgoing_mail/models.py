from django.db import models
from django.utils.text import slugify
import uuid

def rename_outgoing_letter_file(instance, filename):
    ext = filename.split('.')[-1]
    new_filename = f'outgoing_letter_{slugify(instance.letter_number)}_{uuid.uuid4()}.{ext}' 
    return f'outgoing_letter/{new_filename}'

class OutgoingLetter(models.Model):
     agenda_number = models.CharField(max_length=255, blank=True)
     letter_number = models.CharField(max_length=50, blank=True)
     letter_date = models.DateField(blank=True, null=True)
     destination = models.CharField(max_length=255, blank=True)
     subject = models.CharField(max_length=255, blank=True)
     file = models.FileField(upload_to=rename_outgoing_letter_file, blank=True)
     created_at = models.DateTimeField(auto_now_add=True)
     updated_at = models.DateTimeField(auto_now=True)

     def __str__(self):
          return f"Surat Masuk No. {self.letter_number}"

from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.utils.timezone import now

@receiver(pre_save, sender=OutgoingLetter)
def generate_agenda_number(sender, instance, **kwargs):
    if not instance.agenda_number: #jika agenda number kosong
        current_year = now().year
        last_letter = OutgoingLetter.objects.filter(created_at__year=current_year).order_by('-agenda_number').first()

        if last_letter: #jika terdapat surat terakhir
            last_number = int(last_letter.agenda_number.split('/')[-1]) #mengambil nomor surat terakhir
            new_number = last_number + 1 #menambahkan satu
        else: #jika surat baru
            new_number = 1
        instance.agenda_number = f"{current_year}/{new_number:04d}"