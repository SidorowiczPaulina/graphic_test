
from django.contrib.auth.models import User
from django.db import models

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    work_hours_limit = models.PositiveIntegerField()
    availability = models.ManyToManyField('viewer.UserAvailability')

    def __str__(self):
        return self.user.username

# models.py

class Shift(models.Model):
    shift_id = models.AutoField(primary_key=True)
    SHIFT_CHOICES = [
        ('First_Shift', '8:00-16:00'),
        ('Second_Shift', '14:00-22:00'),
    ]
    shift_name = models.CharField(max_length=20, choices=SHIFT_CHOICES)
    hours = models.IntegerField(default=8)
    min_num_workers = models.PositiveIntegerField(default=2)
    max_num_workers = models.PositiveIntegerField(default=3)

    def __str__(self):
        return f"Shift {self.shift_id}"


class UserAvailability(models.Model):
    user_availability_id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    day = models.CharField(max_length=20)
    shift_preferences = models.ForeignKey(Shift, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.username}'s Availability"

class WorkRestrictions(models.Model):
    work_restriction_id = models.AutoField(primary_key=True)
    max_daily_hours = models.PositiveIntegerField(8)
    min_hours_between = models.PositiveIntegerField(12)
    hours_limit = models.PositiveIntegerField(8)

    def __str__(self):
        return f"Work Restrictions {self.work_restriction_id}"

class Schedule(models.Model):
    UniqueID = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    shift_id = models.ForeignKey(Shift, on_delete=models.CASCADE)
    work_date = models.DateField()


    def __str__(self):
        return f"Schedule {self.schedule_id}"