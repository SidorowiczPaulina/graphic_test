from django.contrib.auth import login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.shortcuts import render, redirect
from .models import UserAvailability, Schedule
from .forms import ScheduleForm
from .forms import UserAvailabilityForm
from django.contrib.auth.decorators import login_required, user_passes_test

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})


def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'registration/login.html', {'form': form})


def user_logout(request):
    logout(request)
    return redirect('home')


def base(request):
    return render(request, "base.html")

def is_admin(user):
    return user.is_authenticated and user.is_staff


@user_passes_test(is_admin, login_url='login')
@login_required(login_url='login')
def create_schedule(request):
    user = request.user

    if request.method == "POST":
        form = ScheduleForm(request.POST, user=user)
        if form.is_valid():
            instance = form.save(commit=False)

            if not user.is_authenticated:  # czy użytkownik nie jest zalogowany (czyli jest gość)
                instance.user = None
            else:
                instance.user = user

            instance.save()

            return redirect('create_schedule')
    else:
        form = ScheduleForm()

    return render(request, "schedule/create_schedule.html", {'form': form})

@user_passes_test(is_admin, login_url='login')
@login_required(login_url='login')
def generate_schedule(request):
    # Tutaj umieść logikę do generowania harmonogramu na podstawie dyspozycji użytkowników
    # Możesz skorzystać z funkcji zdefiniowanych w innych częściach kodu.

    # Przykład:
    user_availabilities = UserAvailability.objects.all()
    for availability in user_availabilities:
        # Tutaj dodaj kod do generowania harmonogramu na podstawie dyspozycji
        # Pamiętaj o uwzględnieniu ograniczeń pracy, ilości godzin itp.
        pass  # Placeholder, replace with actual logic

    return redirect('schedule_list')



def enter_availability(request):
    if request.method == 'POST':
        form = UserAvailabilityForm(request.POST)
        if form.is_valid():
            user = request.user
            instance = form.save(commit=False)
            instance.user = user
            instance.save()
            return redirect('availability_list')
    else:
        form = UserAvailabilityForm()
    return render(request, 'schedule/enter_availability.html', {'form': form})



def home(request):
    return render(request, 'home.html')


def root(request):
    return render(request, 'root.html')


def availability_list(request):
    user_availabilities = UserAvailability.objects.filter(user_id=request.user)

    context = {
        'user_availabilities': user_availabilities,
    }

    return render(request, 'schedule/availability_list.html', context)\

@user_passes_test(is_admin, login_url='login')
@login_required(login_url='login')
def schedule_list(request):
    # Tutaj umieść logikę do pobierania i wyświetlania harmonogramu
    # Możesz skorzystać z funkcji zdefiniowanych w innych częściach kodu.

    # Przykład:
    schedule = Schedule.objects.all()

    return render(request, "schedule/schedule_list.html", {'schedule': schedule})