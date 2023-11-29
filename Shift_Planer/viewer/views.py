from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.shortcuts import render, redirect

from .forms import ScheduleForm
from .forms import UserAvailabilityForm


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


@login_required(login_url='login')
def create_schedule(request):
    user = request.user

    if request.method == "POST":
        form = ScheduleForm(request.POST, user=user)
        if form.is_valid():
            instance = form.save(commit=False)

            if not user.is_authenticated:   # czy użytkownik nie jest zalogowany (czyli jest gość)
                instance.user = None
            else:
                instance.user = user

            instance.save()

            return redirect('create_schedule')
    else:
        form = ScheduleForm()

    return render(request, "schedule/create_schedule.html", {'form': form})



def enter_availability(request):
    form = UserAvailabilityForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('availability_list')

    return render(request, 'schedule/enter_availability.html', {'form': form})



def home(request):
    return render(request, 'home.html')