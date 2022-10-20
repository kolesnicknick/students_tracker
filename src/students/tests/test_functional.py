from django.test import TestCase
from django.urls import reverse


class TestContact(TestCase):

    def test_contact_form(self):
        data = {
            'email': 'kolesnik@ss.ua',
            'subject': 'subject',
            'text': 'text'
        }
        response = self.client.get(reverse('contact'), data)
        self.assertEquals(response.status_code, 200)
