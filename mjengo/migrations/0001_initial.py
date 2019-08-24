# Generated by Django 2.2.4 on 2019-08-24 08:08

from django.db import migrations, models
import django.db.models.deletion
import fernet_fields.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('password', fernet_fields.fields.EncryptedTextField(max_length=40)),
                ('contractor_email', models.CharField(max_length=100)),
                ('description', models.TextField(default='no description')),
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
