from django.urls import path
# Importowanie funkcji 'path' do definiowania tras URL.

from django.contrib.auth import views as auth_views
# Importowanie widoków z modułu 'auth_views' Django, które są używane do obsługi funkcji związanych z uwierzytelnianiem.

from . import views
# Importowanie widoków z bieżącego modułu 'views'.

from .views import CustomLoginView, PasswordsChangeView
# Importowanie niestandardowych widoków CustomLoginView i PasswordsChangeView z modułu 'views'.

app_name = 'glowny'
# Definiowanie nazwy aplikacji.

urlpatterns = [
    # Lista tras URL dla aplikacji 'glowny'.

    path('', views.index, name='index'),
    # Trasa URL do widoku 'index' pod adresem głównym aplikacji.

    path('contact/', views.contact, name='contact'),
    # Trasa URL do widoku 'contact' pod adresem '/contact/'.

    path('signup/', views.signup, name='signup'),
    # Trasa URL do widoku 'signup' pod adresem '/signup/'.

    path('o_mnie/', views.omnie, name='omnie'),
    path('polityka/', views.polityka, name='polityka'),

    path('login/', CustomLoginView.as_view(), name='login'),
    # Trasa URL do niestandardowego widoku 'CustomLoginView' pod adresem '/login/'.

    path('logout/', views.user_logout, name='logout'),
    # Trasa URL do widoku 'user_logout' pod adresem '/logout/'.

    path('settings/', views.update, name='update'),
    # Trasa URL do widoku 'update' pod adresem '/settings/'.

    path('password/', PasswordsChangeView.as_view(template_name='update_password.html'), name='update_password'),
    # Trasa URL do niestandardowego widoku 'PasswordsChangeView' pod adresem '/password/' z niestandardowym szablonem 'update_password.html'.

    path('weather/', views.weather_widget, name='weather_widget'),
    # Trasa URL do widoku 'weather_widget' pod adresem '/weather/'.
]
