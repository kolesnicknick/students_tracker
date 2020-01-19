from django.urls import path

from teachers.views import (
    generate_teacher,
    teachers,
    teacher_add,
    teachers_edit
)

urlpatterns = [
    path('gen/', generate_teacher, name='teachers-gen'),
    path('list/', teachers, name='teachers-list'),
    path('add/', teacher_add, name='teachers-add'),
    path('edit/<int:pk>/', teachers_edit, name='teachers-edit'),
]
