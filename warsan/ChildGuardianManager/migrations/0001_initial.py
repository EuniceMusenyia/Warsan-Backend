# Generated by Django 4.2.5 on 2023-09-06 16:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Guardian',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('phone_number', models.CharField(max_length=15)),
                ('location', models.CharField(max_length=100)),
                ('fingerprint', models.ImageField(upload_to='fingerprint_images/')),
                ('fingerprint_details', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Child',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('father_full_name', models.CharField(max_length=100)),
                ('date_of_birth', models.DateTimeField()),
                ('gender', models.CharField(max_length=10)),
                ('guardian', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='ChildGuardianManager.guardian')),
            ],
        ),
    ]
