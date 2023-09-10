# Generated by Django 3.2.6 on 2023-09-09 11:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Healthcare', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='healthworker',
            name='default_country_code',
            field=models.CharField(default='+25261', max_length=6),
        ),
        migrations.AlterField(
            model_name='healthworker',
            name='local_phone_number',
            field=models.CharField(max_length=9, unique=True),
        ),
    ]