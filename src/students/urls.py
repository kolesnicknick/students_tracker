from django.urls import path

from .views import (
    generate_student,
    students,
    students_add,
    students_edit,
    students_delete,
    email
)

urlpatterns = [
    path('gen/', generate_student, name='students-gen'),
    path('list/', students, name='students-list'),
    path('add/', students_add, name='students-add'),
    path('edit/<int:pk>/', students_edit, name='students-edit'),
    path('delete/<int:pk>/', students_delete, name='students-delete'),
    path('contact/', email, name='contact'),
]
