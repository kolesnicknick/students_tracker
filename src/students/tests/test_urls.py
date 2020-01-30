from django.test import SimpleTestCase
from django.urls import reverse, resolve

from students.views import students, students_edit


class TestUrls(SimpleTestCase):

    def test_list_url_is_resolved(self):
        url = reverse('students-list')
        self.assertEquals(resolve(url).func, students)

    def test_edit_student_is_resolved(self):
        url = reverse('students-edit', args=[1])
        self.assertEquals(resolve(url).func, students_edit)
