# Generated by Django 4.2.5 on 2023-11-25 10:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Shift',
            fields=[
                ('shift_id', models.AutoField(primary_key=True, serialize=False)),
                ('shift_name', models.CharField(choices=[('First_Shift', '8:00-16:00'), ('Second_Shift', '14:00-22:00')], max_length=20)),
                ('hours', models.IntegerField(default=8)),
                ('min_num_workers', models.PositiveIntegerField(default=2)),
                ('max_num_workers', models.PositiveIntegerField(default=3)),
            ],
        ),
        migrations.CreateModel(
            name='UserAvailability',
            fields=[
                ('user_availability_id', models.AutoField(primary_key=True, serialize=False)),
                ('day', models.CharField(max_length=20)),
                ('shift_preferences', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='viewer.shift')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='WorkRestrictions',
            fields=[
                ('work_restriction_id', models.AutoField(primary_key=True, serialize=False)),
                ('max_daily_hours', models.PositiveIntegerField(verbose_name=8)),
                ('min_hours_between', models.PositiveIntegerField(verbose_name=12)),
                ('hours_limit', models.PositiveIntegerField(verbose_name=8)),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('work_hours_limit', models.PositiveIntegerField()),
                ('availability', models.ManyToManyField(to='viewer.useravailability')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('UniqueID', models.AutoField(primary_key=True, serialize=False)),
                ('work_date', models.DateField()),
                ('shift_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='viewer.shift')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
