# Generated by Django 2.2.4 on 2019-09-24 19:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myattendance', '0002_studententries_student_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='studententries',
            name='idn',
            field=models.IntegerField(default=0),
        ),
    ]