# Generated by Django 4.2.7 on 2023-11-29 12:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('viewer', '0005_alter_useravailability_day'),
    ]

    operations = [
        migrations.AlterField(
            model_name='useravailability',
            name='day',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='useravailability',
            name='shift_preferences',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='viewer.shift'),
        ),
    ]