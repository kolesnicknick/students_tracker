from django.contrib import admin

from students.admin import StudentInline


class GroupAdmin(admin.ModelAdmin):
    readonly_fields = ('group_name',)
    list_display = ('id', 'group_name', 'senior', 'curator')
    list_select_related = ('senior',)
    list_per_page = 10

    inlines = [
        StudentInline
    ]
