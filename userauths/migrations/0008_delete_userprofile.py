# Generated by Django 4.2.5 on 2023-11-14 21:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userauths', '0007_userprofile'),
    ]

    operations = [
        migrations.DeleteModel(
            name='UserProfile',
        ),
    ]
