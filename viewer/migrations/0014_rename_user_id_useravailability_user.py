# Generated by Django 4.2.7 on 2023-11-29 19:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('viewer', '0013_alter_useravailability_day'),
    ]

    operations = [
        migrations.RenameField(
            model_name='useravailability',
            old_name='user_id',
            new_name='user',
        ),
    ]
