# Generated by Django 2.2.4 on 2019-09-27 05:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myattendance', '0003_studententries_idn'),
    ]

    operations = [
        migrations.AddField(
            model_name='studententries',
            name='percentage',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=4),
        ),
    ]