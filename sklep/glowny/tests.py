from django.test import TestCase
from django.urls import reverse

class IndexViewTest(TestCase):
    def test_index_view(self):

        response = self.client.get(reverse('glowny:index'))
        self.assertEqual(response.status_code, 200)

        self.assertTemplateUsed(response, 'index.html')


class ContactViewTest(TestCase):
    def test_contact_view(self):

        response = self.client.get(reverse('glowny:contact'))
        self.assertEqual(response.status_code, 200)

        self.assertTemplateUsed(response, 'contact.html')


class SignupViewTest(TestCase):
    def test_signup_view_get(self):

        response = self.client.get(reverse('glowny:signup'))
        self.assertEqual(response.status_code, 200)

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


        response = self.client.post(reverse('glowny:signup'), data)
        self.assertEqual(response.status_code, 302)

