# Generated by Django 2.2.4 on 2020-04-29 12:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0004_auto_20200429_1649'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='flat',
            name='Cтарое здание',
        ),
        migrations.AddField(
            model_name='flat',
            name='new_building',
            field=models.NullBooleanField(),
        ),
    ]
