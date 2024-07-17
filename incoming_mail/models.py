from django.db import models

class IncomingLetter(models.Model):
    source = models.CharField(max_length=255)
    recipient = models.CharField(max_length=255)
    letter_number = models.CharField(max_length=50)
    agenda_number = models.CharField(max_length=50, blank=True)
    letter_date = models.DateField()
    received_date = models.DateField()
    file = models.FileField(upload_to='incoming_letter', blank=True)
    subject = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Surat Masuk No. {self.letter_number}"

# from django.db.models.signals import pre_save
# from django.dispatch import receiver
# from django.utils.timezone import now

# @receiver(pre_save, sender=IncomingLetter)
# def generate_agenda_number(sender, instance, **kwargs):
#     if not instance.agenda_number: #jika agenda number kosong
#         current_year = now().year
#         last_letter = IncomingLetter.objects.filter(created_at__year=current_year).order_by('-agenda_number').first()

#         if last_letter: #jika terdapat surat terakhir
#             last_number = int(last_letter.agenda_number.split('/')[-1])
#             new_number = last_number + 1
#         else: #jika surat baru
#             new_number = 1
#         instance.agenda_number = f"{current_year}/{new_number:04d}" 