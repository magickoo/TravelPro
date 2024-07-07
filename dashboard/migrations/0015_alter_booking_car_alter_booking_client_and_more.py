# Generated by Django 4.2.3 on 2024-07-07 06:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('dashboard', '0014_alter_car_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='car',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='dashboard.car'),
        ),
        migrations.AlterField(
            model_name='booking',
            name='client',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='booking',
            name='dropoff_location',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='booking',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
    ]
