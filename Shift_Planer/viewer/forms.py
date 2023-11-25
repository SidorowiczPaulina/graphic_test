from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

class RegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password']

class LoginForm(AuthenticationForm):
    class Meta:
        model = UserCreationForm
        fields = ['username', 'password']