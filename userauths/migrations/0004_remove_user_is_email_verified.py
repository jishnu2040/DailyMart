# Generated by Django 4.2.5 on 2023-11-10 14:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userauths', '0003_user_is_email_verified'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='is_email_verified',
        ),
    ]
