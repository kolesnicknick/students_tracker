from teachers.models import Teacher
from django.contrib import admin


class TeacherAdmin(admin.ModelAdmin):
    readonly_fields = ('email', 'phone')
    list_display = ('id', 'degree', 'first_name', 'last_name', 'email', 'phone')
    list_per_page = 10


admin.site.register(Teacher, TeacherAdmin)
