# Generated by Django 4.0.2 on 2022-02-19 19:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vehicles', '0004_vehicle_staticmap'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vehicle',
            name='staticMap',
            field=models.ImageField(default='', upload_to=''),
        ),
    ]
