# Generated by Django 5.0.1 on 2024-03-01 02:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('rideapp', '0002_delete_customuser'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ride',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rider', models.CharField(max_length=200)),
                ('driver', models.CharField(max_length=200)),
                ('pickup_location', models.CharField(max_length=200)),
                ('dropoff_location', models.CharField(max_length=200)),
                ('status', models.CharField(max_length=200)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
