# Generated by Django 4.2.3 on 2024-07-06 18:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0011_remove_booking_dropoff_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='car',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.car'),
        ),
    ]