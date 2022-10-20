from django.test import TestCase, Client
from django.urls import reverse


class TestViews(TestCase):
    def setUp(self):
        self.client = Client()

    def test_student_list_get(self):
        response = self.client.get(reverse('students-list'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'student_list.html')

    def test_student_edit_get(self):
        client = Client()

        response = self.client.get(reverse('students-edit'))
        self.assertEquals(response.status_code, 302)
        self.assertTemplateUsed(response, 'student_edit.html')
