from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

from .constants import SHIFT_CHOICES
from .models import Schedule
from .models import UserAvailability


class RegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']


class LoginForm(AuthenticationForm):
    class Meta:
        model = User  # Popraw błąd: zmień UserCreationForm na User
        fields = ['username', 'password']


class ScheduleForm(forms.ModelForm):
    class Meta:
        model = Schedule
        fields = ['user', 'work_date']

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super(ScheduleForm, self).__init__(*args, **kwargs)

        if user and not user.is_staff:
            self.fields['work_date'].widget.attrs['readonly'] = True




class UserAvailabilityForm(forms.ModelForm):
    class Meta:
        model = UserAvailability
        fields = ['day', 'shift_preferences']

    shift_preferences = forms.ChoiceField(choices=SHIFT_CHOICES)

    def __init__(self, *args, user=None, **kwargs):
        super(UserAvailabilityForm, self).__init__(*args, **kwargs)

        # Ustaw początkowe dane dla pola 'user'
        if user:
            self.fields['user'] = forms.ModelChoiceField(queryset=User.objects.filter(pk=user.pk), initial=user)