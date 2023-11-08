from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
# Importowanie niezbędnych klas i modeli z modułu 'auth' Django.

from django.db import models


# Importowanie modułu 'models' z Django, który pozwala na definiowanie modeli bazy danych.

class CustomUserManager(BaseUserManager):
    # Definicja niestandardowego managera użytkownika.

    def create_user(self, email, password=None, **extra_fields):
        # Metoda do tworzenia zwykłego użytkownika.
        if not email:
            raise ValueError('Email address is required')
        # Sprawdzenie, czy podano adres email.

        email = self.normalize_email(email)
        # Normalizacja adresu email (np. zamiana na małe litery).

        user = self.model(email=email, **extra_fields)
        # Tworzenie instancji modelu CustomUser.

        user.set_password(password)
        # Ustawienie hasła użytkownika.

        user.save(using=self._db)
        # Zapisanie użytkownika w bazie danych.

        return user

    def create_superuser(self, email, password=None, **extra_fields):
        # Metoda do tworzenia superużytkownika (administratora).
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self.create_user(email, password, **extra_fields)
        # Utworzenie superużytkownika, który posiada uprawnienia administratora.


class CustomUser(AbstractBaseUser, PermissionsMixin):
    # Definicja niestandardowego modelu użytkownika.

    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_premium = models.BooleanField(default=False)
    wojewodztwo = models.CharField(max_length=30, default='')
    miasto = models.CharField(max_length=30, default='')
    ulica = models.CharField(max_length=30, default='')
    nr_domu = models.CharField(max_length=6, default='')
    kod_pocztowy = models.CharField(max_length=6, default='')

    objects = CustomUserManager()  # niestandardowe metody do modelu uzytkownika
    # Przypisanie managera do modelu CustomUser.

    USERNAME_FIELD = 'email'  # unikatowe
    REQUIRED_FIELDS = [] #definiuje wymagane pola do rejestacji

    # Definiowanie pól wymaganych podczas tworzenia użytkownika.

    def __str__(self):
        return self.email
        # Zwracanie adresu email użytkownika jako jego reprezentacji tekstowej (np. w panelu administracyjnym).
