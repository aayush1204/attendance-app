# Generated by Django 2.2.4 on 2019-09-10 19:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='StudentEntries',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject_name', models.CharField(max_length=250, null=True)),
                ('total_lectures', models.IntegerField(default=0)),
                ('attended_lectures', models.IntegerField(default=0)),
                ('missed_lectures', models.IntegerField(default=0)),
            ],
        ),
    ]
