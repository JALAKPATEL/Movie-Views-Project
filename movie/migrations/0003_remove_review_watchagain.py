# Generated by Django 4.2 on 2024-08-28 05:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0002_review'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='review',
            name='watchAgain',
        ),
    ]
