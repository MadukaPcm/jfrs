# Generated by Django 3.2.18 on 2023-03-20 08:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reportdata', '0004_auto_20230320_0049'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='loavessel',
            name='aportDeliveryDateNo',
        ),
    ]
