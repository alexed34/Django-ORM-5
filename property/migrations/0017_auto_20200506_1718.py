# Generated by Django 2.2.4 on 2020-05-06 13:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0016_auto_20200505_1930'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='flat',
            name='owner',
        ),
        migrations.RemoveField(
            model_name='flat',
            name='owner_phone_pure',
        ),
        migrations.RemoveField(
            model_name='flat',
            name='owners_phonenumber',
        ),
    ]
