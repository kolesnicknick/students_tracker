from django.urls import path

from groups.views import (
    generate_group,
    groups,
    group_add,
    group_edit,
    group_delete
)

urlpatterns = [
    path('gen/', generate_group, name='group-gen'),
    path('list/', groups, name='group-list'),
    path('add/', group_add, name='group-add'),
    path('edit/<int:pk>/', group_edit, name='group-edit'),
    path('delete/<int:pk>/', group_delete, name='group-delete'),
]
