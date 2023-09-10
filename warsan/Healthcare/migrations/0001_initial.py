# Generated by Django 3.2.6 on 2023-09-09 09:49

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='HealthWorker',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('local_phone_number', phonenumber_field.modelfields.PhoneNumberField(max_length=10, region=None, unique=True)),
                ('location', models.CharField(max_length=100)),
                ('hospital_name', models.CharField(max_length=100)),
            ],
        ),
    ]
