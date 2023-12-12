from django.test import TestCase
from .models import Schedule

class ScheduleModelTest(TestCase):
    def setUp(self):
        # Przygotuj dane testowe
        Schedule.objects.create(user=None, shift_id=1, work_date='2023-12-01', month=12, year=2023)

    def test_schedule_model(self):
        schedule_entry = Schedule.objects.get(work_date='2023-12-01')
        self.assertEqual(schedule_entry.shift_id, 1)
        self.assertIsNone(schedule_entry.user)
        self.assertEqual(schedule_entry.month, 12)
        self.assertEqual(schedule_entry.year, 2023)