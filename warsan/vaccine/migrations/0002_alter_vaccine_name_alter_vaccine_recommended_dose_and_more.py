# Generated by Django 4.2.5 on 2023-09-11 05:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vaccine', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vaccine',
            name='name',
            field=models.CharField(max_length=32, unique=True),
        ),
        migrations.AlterField(
            model_name='vaccine',
            name='recommended_dose',
            field=models.DecimalField(decimal_places=3, max_digits=6),
        ),
        migrations.AlterField(
            model_name='vaccine',
            name='target_disease',
            field=models.CharField(max_length=32),
        ),
    ]
