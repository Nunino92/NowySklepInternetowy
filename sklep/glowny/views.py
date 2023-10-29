from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView, PasswordChangeView, PasswordResetConfirmView, PasswordResetDoneView, \
    PasswordResetView, PasswordResetCompleteView
from django.core.mail import send_mail
from django.contrib.auth import login, logout
from django.urls import reverse_lazy
from django.shortcuts import render, redirect
import requests
from django.views import View

from przedmioty.models import Category, Item
from .forms import CustomUserCreationForm, UserProfileUpdateForm, PasswordsChangeForm
from django.views.generic import TemplateView

class CustomLoginView(LoginView):
    template_name = 'login.html'

    def form_valid(self, form):
        user = form.get_user()
        login(self.request, user)

        # Wysyłanie e-maila po zalogowaniu
        subject = 'Witaj w naszym serwisie!'
        message = f'Witaj {user.first_name} {user.last_name}! Dziękujemy za zalogowanie się.'
        from_email = 'bajdak123@gmail.com'
        recipient_list = [user.email]

        send_mail(subject, message, from_email, recipient_list, fail_silently=True)

        return super().form_valid(form)

class PasswordsChangeView(PasswordChangeView):
    form_class = PasswordsChangeForm
    success_url = reverse_lazy('glowny:index')

    def form_valid(self, form):
        response = super().form_valid(form)

        subject = 'Zmiana hasła w serwisie'
        message = 'Twoje hasło zostało zmienione.'
        from_email = 'bajdak123@gmail.com'
        recipient_list = [self.request.user.email]

        send_mail(subject, message, from_email, recipient_list, fail_silently=True)

        return response

@login_required
def update(request):
    if request.method == 'POST':
        form = UserProfileUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()

            subject = 'Twoje dane zostały zaktualizowane'
            message = 'Twoje dane w naszym serwisie zostały zaktualizowane.'
            from_email = 'bajdak123@gmail.com'
            recipient_list = [request.user.email]

            send_mail(subject, message, from_email, recipient_list, fail_silently=True)

            return redirect('glowny:index')
    else:
        form = UserProfileUpdateForm(instance=request.user)

    return render(request, 'settings.html', {'form': form})

def index(request):
    items = Item.objects.filter(is_sold=False)[0:6]
    categories = Category.objects.all()

    return render(request, 'index.html', {
        'categories': categories,
        'items': items,
    })

def contact(request):
    return render(request, 'contact.html')

def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('glowny:index')
    else:
        form = CustomUserCreationForm()

    return render(request, 'signup.html', {'form': form})

def user_logout(request):
    logout(request)
    return redirect('glowny:index')


def weather_widget(request):
    api_key = 'fae9322d74e2030d3d8a1911d0eb385d'
    city = request.user.miasto  # Sprawdź, czy to pole istnieje w Twoim modelu użytkownika

    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'

    response = requests.get(url)
    data = response.json()

    temperature = data['main']['temp']
    weather_description = data['weather'][0]['description']

    return render(request, 'weather_widget.html', {
        'temperature': temperature,
        'weather_description': weather_description,
    })
