from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

# Definicja tras (URL patterns) dla aplikacji w projekcie Django.
urlpatterns = [
    path('', include('glowny.urls')),  # Trasa do aplikacji 'glowny'.
    path('items/', include('przedmioty.urls')),  # Trasa do aplikacji 'przedmioty'.
    path('dashboard/', include('panel.urls')),  # Trasa do aplikacji 'panel'.
    path('admin/', admin.site.urls),  # Trasa do panelu admina.
    path('konto/', include('konto.urls')),  # Trasa do aplikacji 'konto'.
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)  # Obsługa plików media w trybie deweloperskim.

# Ta część trasy dodaje obsługę plików media w trybie deweloperskim, co jest przydatne do wyświetlania obrazów itp.