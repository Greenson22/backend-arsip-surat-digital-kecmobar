# Generated by Django 5.0.6 on 2024-07-23 12:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_management', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='photo_url',
            field=models.FileField(blank=True, upload_to='profile'),
        ),
    ]
