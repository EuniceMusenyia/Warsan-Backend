# Generated by Django 3.2.6 on 2023-09-09 17:05

from django.db import migrations
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('Healthcare', '0004_alter_healthworker_local_phone_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='healthworker',
            name='local_phone_number',
            field=phonenumber_field.modelfields.PhoneNumberField(max_length=128, region='SO', unique=True),
        ),
    ]
