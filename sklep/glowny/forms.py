from django import forms
# Importowanie modułu 'forms' z Django, który pozwala na tworzenie formularzy.

from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
# Importowanie różnych formularzy z Django dotyczących uwierzytelniania i zarządzania hasłem użytkownika.

from .models import CustomUser
# Importowanie modelu 'CustomUser' z bieżącej aplikacji (lokalnie).

from .widget import WeatherWidgetForm
# Importowanie formularza 'WeatherWidgetForm' z lokalnego modułu 'widget'.

# Tworzenie formularza CustomUserCreationForm, który dziedziczy po UserCreationForm z Django.
class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('email', 'first_name', 'last_name', 'wojewodztwo', 'miasto', 'ulica', 'nr_domu', 'kod_pocztowy')
    # Definiowanie pola 'Meta', które określa model (CustomUser) i pola, które będą dostępne w formularzu.

# Tworzenie formularza UserProfileUpdateForm, który dziedziczy po ModelForm z Django.
class UserProfileUpdateForm(forms.ModelForm):
    first_name = forms.CharField(max_length=30, required=True, label='First Name')
    last_name = forms.CharField(max_length=30, required=True, label='Last Name')

    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name', 'email', 'wojewodztwo', 'miasto', 'ulica', 'nr_domu', 'kod_pocztowy']
    # Definiowanie pól formularza oraz ich atrybutów w klasie Meta.

# Tworzenie formularza PasswordsChangeForm, który dziedziczy po PasswordChangeForm z Django.
class PasswordsChangeForm(PasswordChangeForm):
    old_password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'type': 'password'}))
    new_password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'type': 'password'}))
    new_password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'type': 'password'}))

    class Meta:
        model = CustomUser.password
        fields = ('old_password', 'new_password1', 'new_password2')
    # Definiowanie formularza zmiany hasła i dostosowanie jego pól oraz atrybutów.

# Tworzenie formularza MyForm, który dziedziczy po forms.Form z Django.
class MyForm(forms.Form):
    some_field = forms.CharField(label='Some Field')
    weather_location = WeatherWidgetForm()
    # Definiowanie dwóch pól formularza: 'some_field' i 'weather_location' z użyciem 'WeatherWidgetForm'.

