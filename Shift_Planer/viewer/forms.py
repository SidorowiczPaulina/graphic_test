from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .models import Schedule, UserAvailability



class RegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']


class LoginForm(AuthenticationForm):
    class Meta:
        model = UserCreationForm
        fields = ['username', 'password']


class ScheduleForm(forms.ModelForm):
    class Meta:
        model = Schedule
        fields = ['user', 'work_date', 'shift_start', 'shift_end']

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super(ScheduleForm, self).__init__(*args, **kwargs)

        if user and not user.is_staff:
            self.fields['work_date'].widget.attrs['readonly'] = True
            self.fields['shift_start'].widget.attrs['readonly'] = True
            self.fields['shift_end'].widget.attrs['readonly'] = True




class UserAvailabilityForm(forms.ModelForm):
    class Meta:
        model = UserAvailability
        fields = ['day', 'shift_preferences']




