# Generated by Django 3.2.6 on 2021-08-16 00:32

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vehicle_garage', '0002_truck'),
    ]

    operations = [
        migrations.CreateModel(
            name='Boat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('boat_make', models.CharField(max_length=50)),
                ('boat_model', models.CharField(max_length=50)),
                ('boat_year', models.PositiveIntegerField(default=0)),
                ('boat_length', models.PositiveIntegerField(default=0)),
                ('boat_width', models.PositiveIntegerField(max_length=50)),
                ('boat_hin', models.CharField(max_length=17)),
                ('boat_curr_hours', models.PositiveIntegerField(default=0)),
                ('boat_service_interval', models.PositiveIntegerField(default=0)),
                ('boat_next_service', models.DateField(default=datetime.date.today)),
            ],
        ),
    ]