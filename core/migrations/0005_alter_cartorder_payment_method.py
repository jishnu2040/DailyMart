# Generated by Django 4.1.7 on 2023-11-29 15:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_alter_cartorder_payment_method'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cartorder',
            name='payment_method',
            field=models.CharField(choices=[('Razorpay', 'Razorpay'), ('Cod', 'Cash on Delivery')], default='Razorpay', max_length=10),
        ),
    ]