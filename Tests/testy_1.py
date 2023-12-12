from datetime import date

import pytest
from django.contrib.auth.models import User
from django.urls import reverse

from .models import Schedule, Shift


@pytest.fixture
def sample_user():
    return User.objects.create_user(username='testuser', password='testpassword')

@pytest.fixture
def sample_shift():
    return Shift.objects.create(shift_name='Morning Shift', hours=8)

@pytest.fixture
def sample_schedule(sample_user, sample_shift):
    return Schedule.objects.create(user=sample_user, shift_id=sample_shift, work_date=date.today())

@pytest.mark.django_db
def test_create_schedule(client, sample_user, sample_shift):
    client.force_login(sample_user)
    response = client.post(reverse('create_schedule'), {'user': sample_user.id, 'shift_id': sample_shift.id, 'work_date': date.today()})
    assert response.status_code == 302  # Redirect status code

    # Sprawdź, czy nowy wpis w grafiku został utworzony
    assert Schedule.objects.count() == 1

@pytest.mark.django_db
def test_generate_schedule(client, sample_user, sample_shift):
    client.force_login(sample_user)
    response = client.post(reverse('generate_schedule'))
    assert response.status_code == 200

    # Sprawdź, czy generowanie grafiku działa poprawnie
    assert Schedule.objects.count() > 0

@pytest.mark.django_db
def test_view_schedule(client, sample_schedule):
    response = client.get(reverse('view_schedule'))
    assert response.status_code == 200

    # Sprawdź, czy strona zawiera informacje o grafiku użytkownika
    assert str(sample_schedule) in response.content.decode()

# Dodaj więcej testów w miarę potrzeb
