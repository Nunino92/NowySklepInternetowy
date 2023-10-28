from django.test import TestCase
from django.urls import reverse

class IndexViewTest(TestCase):
    def test_index_view(self):
        # Sprawdź czy widok index jest dostępny i zwraca status 200
        response = self.client.get(reverse('glowny:index'))
        self.assertEqual(response.status_code, 200)
        # Sprawdź, czy widok używa szablonu 'index.html'
        self.assertTemplateUsed(response, 'index.html')
        # Dodaj testy, które sprawdzają treść wygenerowanej strony

class ContactViewTest(TestCase):
    def test_contact_view(self):
        # Sprawdź czy widok contact jest dostępny i zwraca status 200
        response = self.client.get(reverse('glowny:contact'))
        self.assertEqual(response.status_code, 200)
        # Sprawdź, czy widok używa szablonu 'contact.html'
        self.assertTemplateUsed(response, 'contact.html')
        # Dodaj testy, które sprawdzają treść wygenerowanej strony

class SignupViewTest(TestCase):
    def test_signup_view_get(self):
        # Sprawdź czy widok signup (GET) jest dostępny i zwraca status 200
        response = self.client.get(reverse('glowny:signup'))
        self.assertEqual(response.status_code, 200)
        # Sprawdź, czy widok używa szablonu 'signup.html'
        self.assertTemplateUsed(response, 'signup.html')

    def test_signup_view_post(self):
        data = {
            'email': 'nowy_uzytkownik@example.com',
            'first_name': 'Imie',
            'last_name': 'Nazwisko',
            'wojewodztwo': 'Mazowieckie',
            'miasto': 'Warszawa',
            'ulica': 'ul. Przykładowa 123',
            'nr_domu': '123',
            'kod_pocztowy': '00-000',
            'password1': 'nowe_haslo123',
            'password2': 'nowe_haslo123',
        }

        # Sprawdź czy widok signup (POST) przyjmuje dane formularza i zwraca status 200
        response = self.client.post(reverse('glowny:signup'), data)
        self.assertEqual(response.status_code, 302)  # Tutaj może być błąd, warto sprawdzić, czy przekierowuje po poprawnej rejestracji
        # Dodaj testy, które sprawdzają, czy użytkownik został poprawnie zarejestrowany
