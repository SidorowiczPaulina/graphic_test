import pytest
from django.test import Client

client = Client()
@pytest.mark.django_db
def test_create_schedule(client, sample_user, sample_shift):
    client.force_login(sample_user)
    response = client.post(reverse('create_schedule'), {'user': sample_user.id, 'shift_id': sample_shift.id, 'work_date': date.today()})
    assert response.status_code == 302  # Redirect status code

    # Sprawdź, czy nowy wpis w grafiku został utworzony
    assert Schedule.objects.count() == 1

    # Dodatkowa asercja: Sprawdź, czy utworzony wpis ma oczekiwane wartości
    created_schedule = Schedule.objects.first()
    assert created_schedule.user == sample_user
    assert created_schedule.shift_id == sample_shift
    assert created_schedule.work_date == date.today()

@pytest.mark.django_db
def test_generate_schedule(client, sample_user, sample_shift):
    client.force_login(sample_user)
    response = client.post(reverse('generate_schedule'))
    assert response.status_code == 200

    # Sprawdź, czy generowanie grafiku działa poprawnie
    assert Schedule.objects.count() > 0

    # Dodatkowa asercja: Sprawdź, czy liczba utworzonych wpisów jest zgodna z oczekiwaną
    generated_schedules = Schedule.objects.filter(user=sample_user)
    assert generated_schedules.count() > 0

@pytest.mark.django_db
def test_view_schedule(client, sample_schedule):
    response = client.get(reverse('view_schedule'))
    assert response.status_code == 200

    # Sprawdź, czy strona zawiera informacje o grafiku użytkownika
    assert str(sample_schedule) in response.content.decode()

@pytest.mark.django_db
def test_view_schedule_unauthenticated(client):
    response = client.get(reverse('view_schedule'))
    assert response.status_code in [302, 200]  # Przekierowanie dla niezalogowanego użytkownika

@pytest.mark.django_db
def test_generate_schedule_unauthenticated(client):
    response = client.post(reverse('generate_schedule'))
    assert response.status_code == 302  # Przekierowanie dla niezalogowanego użytkownika
