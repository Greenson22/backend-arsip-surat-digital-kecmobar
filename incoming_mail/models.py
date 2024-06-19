from django.db import models

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
    agenda_number = models.CharField(max_length=50)
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