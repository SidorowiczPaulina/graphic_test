# Generated by Django 4.2.7 on 2023-11-29 19:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('viewer', '0012_alter_useravailability_shift_preferences'),
    ]

    operations = [
        migrations.AlterField(
            model_name='useravailability',
            name='day',
            field=models.DateField(blank=True),
        ),
    ]
