# Generated by Django 5.1.2 on 2024-10-26 18:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chat_app', '0004_userprofile'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Message',
        ),
    ]
