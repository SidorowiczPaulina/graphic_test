# Generated by Django 4.2.7 on 2023-11-29 13:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('viewer', '0006_alter_useravailability_day_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='useravailability',
            name='shift_preferences',
            field=models.ForeignKey(choices=[('First_Shift', '8:00-16:00'), ('Second_Shift', '14:00-22:00')], on_delete=django.db.models.deletion.CASCADE, to='viewer.shift'),
        ),
    ]
