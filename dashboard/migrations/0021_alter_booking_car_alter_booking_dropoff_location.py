# Generated by Django 4.2.3 on 2024-07-07 06:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0020_alter_booking_client_alter_booking_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='car',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.car'),
        ),
        migrations.AlterField(
            model_name='booking',
            name='dropoff_location',
            field=models.CharField(max_length=255),
        ),
    ]
