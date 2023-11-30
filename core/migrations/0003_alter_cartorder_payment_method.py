# Generated by Django 4.1.7 on 2023-11-29 05:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_cartorder_payment_id_alter_cartorder_payment_method'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cartorder',
            name='payment_method',
            field=models.CharField(choices=[('Razorpay', 'Razorpay'), ('Cod', 'Cash on Delivery')], default='Razorpay', max_length=10),
        ),
    ]
