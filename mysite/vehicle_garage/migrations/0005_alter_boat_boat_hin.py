# Generated by Django 3.2.6 on 2021-08-20 20:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vehicle_garage', '0004_alter_boat_boat_width'),
    ]

    operations = [
        migrations.AlterField(
            model_name='boat',
            name='boat_hin',
            field=models.CharField(max_length=12),
        ),
    ]
