from django import forms
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from .models import CustomUser
from .widget import WeatherWidgetForm


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('email', 'first_name', 'last_name', 'wojewodztwo', 'miasto', 'ulica', 'nr_domu', 'kod_pocztowy')


class UserProfileUpdateForm(forms.ModelForm):
    first_name = forms.CharField(max_length=30, required=True, label='First Name')
    last_name = forms.CharField(max_length=30, required=True, label='Last Name')

    class Meta:
        model = CustomUser  # Zakłada, że Twoim modelem użytkownika jest User.
        fields = ['first_name', 'last_name', 'email', 'wojewodztwo', 'miasto', 'ulica', 'nr_domu', 'kod_pocztowy']


class PasswordsChangeForm(PasswordChangeForm):
    old_password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'type': 'password'}))
    new_password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'type': 'password'}))
    new_password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'type': 'password'}))

    class Meta:
        model = CustomUser.password
        fields = ('old_password', 'new_password1', 'new_password2')

class MyForm(forms.Form):
    some_field = forms.CharField(label='Some Field')
    weather_location = WeatherWidgetForm()