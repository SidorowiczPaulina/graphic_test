from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .constants import SHIFT_CHOICES
from .models import Schedule
from .models import UserAvailability
from django.forms.widgets import DateInput
from django.db.models import Sum
from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django.core.exceptions import ValidationError

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
        fields = ['user']

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super(ScheduleForm, self).__init__(*args, **kwargs)

        if user and not user.is_staff:
            self.fields['work_date'].widget = DateInput(attrs={'type': 'date'})  # Zmiana widgetu

            # Usuń pole user dla zwykłego użytkownika
            del self.fields['user']

            # Usuń pole UniqueID
            del self.fields['UniqueID']

    your_date_field = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'text', 'class': 'datepicker'}),
        input_formats=['%Y-%m-%d'],
    )


    def save(self, commit=True):
        # Ustaw pole user na None dla zwykłego użytkownika
        if not self.instance.user.is_staff:
            self.instance.user = None

        return super(ScheduleForm, self).save(commit)





class UserAvailabilityForm(forms.ModelForm):
    class Meta:
        model = UserAvailability
        fields = ['user_id', 'day', 'shift_preferences']

    shift_preferences = forms.ChoiceField(choices=SHIFT_CHOICES)
    day = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))

    def init(self, args, user=None, **kwargs):
        super(UserAvailabilityForm, self).init(args, **kwargs)

        # Ustaw początkowe dane dla pola 'user_id'
        if user:
            self.fields['user_id'] = forms.ModelChoiceField(queryset=User.objects.filter(pk=user.pk), initial=user)

    def clean(self):
        cleaned_data = super().clean()
        user = cleaned_data.get('user_id')
        day = cleaned_data.get('day')

        # Sprawdź, czy istnieje już dyspozycja dla danego użytkownika na ten dzień
        existing_availability = UserAvailability.objects.filter(user_id=user, day=day).exists()

        if existing_availability:
            raise ValidationError('Dyspozycja dla tego użytkownika na ten dzień już istnieje.')

        return cleaned_data
class AvailabilitySelectionForm(forms.ModelForm):
    class Meta:
        model = UserAvailability
        fields = ['day', 'shift_preferences']


