# Generated by Django 4.0.2 on 2022-02-19 19:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vehicles', '0008_remove_vehicle_staticmap'),
    ]

    operations = [
        migrations.AddField(
            model_name='vehicle',
            name='maps',
            field=models.ImageField(default=None, upload_to=''),
        ),
    ]