# Generated by Django 4.2.5 on 2023-09-27 06:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vaccine', '0002_alter_vaccine_name_alter_vaccine_recommended_dose_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vaccine',
            name='maximum_age',
        ),
        migrations.RemoveField(
            model_name='vaccine',
            name='minimum_age',
        ),
        migrations.RemoveField(
            model_name='vaccine',
            name='recommended_dose',
        ),
    ]
