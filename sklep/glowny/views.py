import requests
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.views import LoginView, PasswordChangeView
from django.shortcuts import render, redirect
from django.contrib.auth import logout, login, update_session_auth_hash
from django.urls import reverse_lazy

from przedmioty.models import Category, Item

from .forms import CustomUserCreationForm, UserProfileUpdateForm, PasswordsChangeForm


class CustomLoginView(LoginView):
    template_name = 'login.html'

    def form_valid(self, form):
        user = form.get_user()
        login(self.request, user)
        return super().form_valid(form)
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

@login_required
def update(request):
    if request.method == 'POST':
        form = UserProfileUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('glowny:index')  # Przekieruj na odpowiednią stronę po udanej aktualizacji
    else:
        form = UserProfileUpdateForm(instance=request.user)

    return render(request, 'settings.html', {'form': form})


@login_required
def update_password(request):
    if request.method == 'POST':
        form = CustomPasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # To keep the user logged in
            messages.success(request, 'Your password was successfully updated!')
            return redirect('glowny:update_password')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = CustomPasswordChangeForm(request.user)
    return render(request, 'update_password.html', {'form': form})



class PasswordsChangeView(PasswordChangeView):
    form_class = PasswordsChangeForm
    success_url = reverse_lazy('glowny:index')



def weather_widget(request):
    api_key = 'fae9322d74e2030d3d8a1911d0eb385d'
    city = request.user.miasto   # Zmień na miasto, dla którego chcesz wyświetlać pogodę

    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'

    response = requests.get(url)
    data = response.json()

    temperature = data['main']['temp']
    weather_description = data['weather'][0]['description']

    return render(request, 'weather_widget.html', {
        'temperature': temperature,
        'weather_description': weather_description,
    })
