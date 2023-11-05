from django.contrib import admin
# Importowanie modułu 'admin' z Django, który umożliwia zarządzanie danymi w panelu administracyjnym.

from .models import CustomUser

# Importowanie modelu 'CustomUser' z bieżącej aplikacji (lokalnie).

# Rejestracja modelu w panelu administracyjnym Django.
admin.site.register(CustomUser)
# Dzięki tej linii kodu model 'CustomUser' zostaje zarejestrowany w panelu administracyjnym, co pozwala na zarządzanie użytkownikami za pomocą interfejsu dostępnego na stronie /admin/ Twojej aplikacji.

# To jest standardowy sposób rejestrowania modeli w panelu administracyjnym Django.
