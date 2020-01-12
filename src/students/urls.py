from django.urls import path

from .views import (
    generate_student,
    students,
    students_add,
    students_edit
)

urlpatterns = [
    path('generate_s/', generate_student, name='students-gen'),
    path('list/', students, name='students'),
    path('students/add/', students_add, name='students-add'),
    path('students/edit/<int:pk>', students_edit, name='students-edit'),
]
