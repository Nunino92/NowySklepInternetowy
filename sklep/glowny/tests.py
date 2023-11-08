from django.test import SimpleTestCase
from django.urls import resolve, reverse
from . import views
from django.test import TestCase
from .forms import CustomUserCreationForm
from django.contrib.auth import get_user_model



#1.

class GlownyUrlsTest(SimpleTestCase):
    def test_index_url(self):
        url = reverse('glowny:index')
        # Porównaj funkcję obsługującą ten URL z oczekiwanym widokiem 'index'.
        self.assertEqual(resolve(url).func, views.index)

    def test_contact_url(self):
        url = reverse('glowny:contact')
        self.assertEqual(resolve(url).func, views.contact)

    def test_signup_url(self):
        url = reverse('glowny:signup')
        self.assertEqual(resolve(url).func, views.signup)

    def test_login_url(self):
        url = reverse('glowny:login')
        self.assertEqual(resolve(url).func.view_class, views.CustomLoginView)

    def test_logout_url(self):
        url = reverse('glowny:logout')
        self.assertEqual(resolve(url).func, views.user_logout)

    def test_update_url(self):
        url = reverse('glowny:update')
        self.assertEqual(resolve(url).func, views.update)

    def test_update_password_url(self):
        url = reverse('glowny:update_password')
        self.assertEqual(resolve(url).func.view_class, views.PasswordsChangeView)

    def test_weather_widget_url(self):
        url = reverse('glowny:weather_widget')
        self.assertEqual(resolve(url).func, views.weather_widget)

#2.
class IndexViewTest(TestCase):
    #Czy zwraca kod 200 - ok oraz czy dostepny jest strona głowna
    def test_index_view(self):
        # Wykonaj żądanie GET do widoku 'index' w aplikacji 'glowny' za pomocą klienta testowego.
        response = self.client.get(reverse('glowny:index'))
        # Sprawdź, czy status HTTP odpowiedzi to 200 (OK).
        self.assertEqual(response.status_code, 200)
        # Sprawdź, czy używany jest oczekiwany szablon 'index.html'.
        self.assertTemplateUsed(response, 'index.html')


class ContactViewTest(TestCase):
    #Zwraca kod 200 oraz dostep do strony contract.html
    def test_contact_view(self):
        response = self.client.get(reverse('glowny:contact'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'contact.html')


#3.

class SignupViewTest(TestCase):
    #Zwraca kod 200 oraz dostep do strony singup.html
    def test_signup_view_get(self):

        response = self.client.get(reverse('glowny:signup'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'signup.html')

    #Sprawdza czy działa rejestracja i kod 200
    def test_signup_view_post(self):
        data = {
            'email': 'uzytkownik@przyklad.com',
            'first_name': 'Imie',
            'last_name': 'Nazwisko',
            'wojewodztwo': 'Krakowskie',
            'miasto': 'Krakow',
            'ulica': 'ul. Przykładowa 123',
            'nr_domu': '123',
            'kod_pocztowy': '00-000',
            'password1': 'haslo123123',
            'password2': 'haslo123123',
        }


        response = self.client.post(reverse('glowny:signup'), data)
        # Wykonaj żądanie POST do widoku 'signup' w aplikacji 'glowny' z danymi przesłanymi jako 'data'.
        self.assertEqual(response.status_code, 302)
        # Sprawdź, czy status HTTP odpowiedzi to 302 (przekierowanie).

#4.
class CustomUserTestCase(TestCase):
    def setUp(self):
        # Przygotowanie danych testowych
        self.user = CustomUser.objects.create(email="testuser@example.com", first_name="Test", last_name="User")

    def test_index_view(self):
        # Test, który sprawdza, czy widok 'index' zwraca kod stanu HTTP 200 (sukces).
        response = self.client.get(reverse('glowny:index'))
        self.assertEqual(response.status_code, 200)

    def test_login_view(self):
        # Test, który sprawdza, czy widok 'login' zwraca kod stanu HTTP 200 (sukces).
        response = self.client.get(reverse('glowny:login'))
        self.assertEqual(response.status_code, 200)

    def test_logout_view(self):
        # Test, który sprawdza, czy widok 'logout' zwraca kod stanu HTTP 302 (przekierowanie).
        response = self.client.get(reverse('glowny:logout'))
        self.assertEqual(response.status_code, 302)

    def test_user_profile_update_view(self):
        # Test, który sprawdza, czy widok 'update' zwraca kod stanu HTTP 200 (sukces) dla zalogowanego użytkownika.
        self.client.force_login(self.user)
        response = self.client.get(reverse('glowny:update'))
        self.assertEqual(response.status_code, 200)

    def test_user_profile_update_view_unauthenticated(self):
        # Test, który sprawdza, czy widok 'update' przekierowuje niezalogowanego użytkownika do strony logowania.
        response = self.client.get(reverse('glowny:update'))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('glowny:login') + f'?next={reverse("glowny:update")}')



class CustomUserFormTestCase(TestCase):
    def test_custom_user_creation_form_valid_data(self):
        # Test sprawdzający, czy formularz CustomUserCreationForm działa poprawnie z poprawnymi danymi.
        data = {
            'email': 'test@example.com',
            'first_name': 'John',
            'last_name': 'Doe',
            'password1': 'securepassword123',
            'password2': 'securepassword123',
        }
        form = CustomUserCreationForm(data=data)
        self.assertTrue(form.is_valid())

    def test_custom_user_creation_form_invalid_data(self):
        # Test sprawdzający, czy formularz CustomUserCreationForm nie akceptuje błędnych danych.
        data = {
            'email': 'invalid-email',  # Niepoprawny adres email
            'password1': 'password123',
            'password2': 'differentpassword',  # Różne hasła
        }
        form = CustomUserCreationForm(data=data)
        self.assertFalse(form.is_valid())

class CustomUserModelTestCase(TestCase):
    def test_custom_user_str_method(self):
        # Test, który sprawdza, czy metoda __str__() w modelu CustomUser działa poprawnie.
        user = CustomUser.objects.create(email='test@example.com', first_name='John', last_name='Doe')
        self.assertEqual(str(user), 'test@example.com')

    def test_custom_user_creation(self):
        # Test tworzenia niestandardowego użytkownika.
        user = CustomUser.objects.create_user(email='test@example.com', password='securepassword123')
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)
        self.assertTrue(user.is_active)

class LoginTestCase(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(email='test@example.com', password='securepassword123')

    def test_login_view_authenticated_user(self):
        # Test, który sprawdza, czy zalogowany użytkownik jest przekierowywany z widoku logowania.
        self.client.force_login(self.user)
        response = self.client.get(reverse('glowny:login'))
        self.assertRedirects(response, reverse('glowny:index'))

    def test_login_view_unauthenticated_user(self):
        # Test, który sprawdza, czy niezalogowany użytkownik ma dostęp do widoku logowania.
        response = self.client.get(reverse('glowny:login'))
        self.assertEqual(response.status_code, 200)


'''
1. reverse()znalezienie kodu po views -> resolve()sprawdza czy dobrze przypisany 
2. wysyła zapytanie get poprzez reverse -> status 200 i czy uzyty index.html
3. rejestracja uzytkownika na przypadkowych danych
4. 

'''