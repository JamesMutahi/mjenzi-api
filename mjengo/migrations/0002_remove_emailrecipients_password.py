# Generated by Django 2.2.4 on 2019-08-26 08:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mjengo', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='emailrecipients',
            name='password',
        ),
    ]
