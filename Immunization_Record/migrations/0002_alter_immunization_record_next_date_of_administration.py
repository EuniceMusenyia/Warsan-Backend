# Generated by Django 4.2.5 on 2023-09-25 12:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Immunization_Record', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='immunization_record',
            name='next_date_of_administration',
            field=models.DateTimeField(),
        ),
    ]