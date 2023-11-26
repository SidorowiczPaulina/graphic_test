from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from .forms import UserAvailabilityForm, ScheduleForm


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


def create_schedule(request):
    if request.method == "POST":
        form = ScheduleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('create_schedule')
    else:
        form = ScheduleForm()
    return render(request, "schedule/create_schedule.html", {'form': form})


def enter_availability(request):
    if request.method == 'POST':
        form = UserAvailabilityForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('availability_list')
    else:
        form = UserAvailabilityForm()
    return render(request, 'enter_availability.html', {'form': form})


def home(request):
    return render(request, 'home.html')
