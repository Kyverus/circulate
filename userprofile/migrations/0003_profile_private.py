# Generated by Django 5.1.5 on 2025-01-25 06:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0002_profile_avatar'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='private',
            field=models.BooleanField(default=True),
        ),
    ]
