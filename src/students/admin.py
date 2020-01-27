from django.contrib import admin

from groups.models import Group
from students.forms import StudentsAdminForm
from students.models import Student
from teachers.models import Teacher


class StudentAdmin(admin.ModelAdmin):
    # readonly_fields = ('emails', 'groups')
    list_display = ('id', 'first_name', 'last_name', 'groups',)
    list_select_related = ('groups',)
    list_per_page = 10
    form = StudentsAdminForm

    def get_readonly_fields(self, request, obj=None):
        readonly_fields = super().get_readonly_fields(request, obj)
        if request.user.groups.filter(name='manager').exists():
            return readonly_fields + ('phone',)
        return readonly_fields

    def has_delete_permission(self, request, obj=None):
        return False


class StudentInline(admin.TabularInline):
    model = Student


class GroupAdmin(admin.ModelAdmin):
    inlines = [
        StudentInline
    ]


class TeacherAdmin(admin.ModelAdmin):
    pass


admin.site.register(Student, StudentAdmin)
admin.site.register(Teacher, TeacherAdmin)
admin.site.register(Group, GroupAdmin)
