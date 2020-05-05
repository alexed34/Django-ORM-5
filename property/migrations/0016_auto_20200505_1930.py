# Generated by Django 2.2.4 on 2020-05-05 15:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0015_auto_20200505_1749'),
    ]

    operations = [
        migrations.AlterField(
            model_name='owner',
            name='flat',
            field=models.ManyToManyField(db_index=True, null=True, related_name='owner_flats', to='property.Flat', verbose_name='Квартиры в собственности'),
        ),
        migrations.AlterField(
            model_name='owner',
            name='owner',
            field=models.CharField(db_index=True, max_length=200, null=True, verbose_name='ФИО владельца'),
        ),
    ]
