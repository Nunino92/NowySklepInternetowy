from django.test import TestCase
from django.urls import reverse

class IndexViewTest(TestCase):
    #Czy zwraca kod 200 - ok oraz czy dostepny jest strona głowna
    def test_index_view(self):

        response = self.client.get(reverse('glowny:index'))
        self.assertEqual(response.status_code, 200)

        self.assertTemplateUsed(response, 'index.html')


class ContactViewTest(TestCase):
    #Zwraca kod 200 oraz dostep do strony contract.html
    def test_contact_view(self):

        response = self.client.get(reverse('glowny:contact'))
        self.assertEqual(response.status_code, 200)

        self.assertTemplateUsed(response, 'contact.html')


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
        self.assertEqual(response.status_code, 302)

