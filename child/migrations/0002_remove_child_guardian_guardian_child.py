# Generated by Django 4.2.5 on 2023-09-25 16:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('child', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='child',
            name='guardian',
        ),
        migrations.AddField(
            model_name='guardian',
            name='child',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='child.child'),
        ),
    ]