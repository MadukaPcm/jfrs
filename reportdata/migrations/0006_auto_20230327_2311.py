# Generated by Django 3.2.18 on 2023-03-28 06:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reportdata', '0005_remove_loavessel_aportdeliverydateno'),
    ]

    operations = [
        migrations.AddField(
            model_name='loafum',
            name='isDone',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='loavessel',
            name='isDone',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='openf',
            name='isDone',
            field=models.BooleanField(default=False),
        ),
    ]
