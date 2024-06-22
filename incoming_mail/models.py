from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.utils.timezone import now

class Recipient(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Source(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class IncomingLetter(models.Model):
    letter_number = models.CharField(max_length=50)
    agenda_number = models.CharField(max_length=50, blank=True)
    letter_date = models.DateField()
    received_date = models.DateField()
    recipient = models.ForeignKey(Recipient, on_delete=models.CASCADE)
    source = models.ForeignKey(Source, on_delete=models.CASCADE)
    file_url = models.URLField(blank=True, null=True)  # Optional
    subject = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Surat Masuk No. {self.letter_number}"

@receiver(pre_save, sender=IncomingLetter)
def generate_agenda_number(sender, instance, **kwargs):
    if not instance.agenda_number: #jika agenda number kosong
        current_year = now().year
        last_letter = IncomingLetter.objects.filter(created_at__year=current_year).order_by('-agenda_number').first()

        if last_letter: #jika terdapat surat terakhir
            last_number = int(last_letter.agenda_number.split('/')[-1])
            new_number = last_number + 1
        else: #jika surat baru
            new_number = 1
        instance.agenda_number = f"{current_year}/{new_number:04d}" 