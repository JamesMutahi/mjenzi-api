# Generated by Django 2.2.4 on 2019-08-23 09:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('password', models.CharField(max_length=40)),
                ('contractor_email', models.CharField(max_length=100)),
                ('description', models.TextField(default='no description')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Requests',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('Cement', 'Cement'), ('Brick', 'Brick'), ('Sand', 'Sand'), ('Ballast', 'Ballast'), ('Metal rods', 'Metal rods'), ('Roofing tiles', 'Roofing tiles')], default='Cement', max_length=20)),
                ('quantity', models.IntegerField()),
                ('photo', models.ImageField(default='projects/default.jpeg', upload_to='projects')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mjengo.Project')),
            ],
        ),
        migrations.CreateModel(
            name='Materials',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('Cement', 'Cement'), ('Brick', 'Brick'), ('Sand', 'Sand'), ('Ballast', 'Ballast'), ('Metal rods', 'Metal rods'), ('Roofing tiles', 'Roofing tiles')], default='Cement', max_length=20)),
                ('quantity', models.IntegerField()),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mjengo.Project')),
            ],
        ),
    ]
