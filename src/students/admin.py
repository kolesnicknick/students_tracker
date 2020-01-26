from django.contrib import admin

from groups.models import Group
from students.models import Student
from teachers.models import Teacher


class StudentAdmin(admin.ModelAdmin):
    readonly_fields = ('emails', 'groups')
    last_display = ('id', 'first_name', 'last_name', 'groups',)
    list_select_related = ('groups',)
    list_per_page = 10

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
    readonly_fields = ('group_name',)
    list_display = ('id', 'group_name', 'senior', 'curator')
    list_select_related = ('senior',)
    list_per_page = 10

    inlines = [
        StudentInline
    ]


class TeacherAdmin(admin.ModelAdmin):
    readonly_fields = ('email', 'phone')
    list_display = ('id', 'degree', 'first_name', 'last_name', 'email', 'phone')
    list_per_page = 10


admin.site.register(Student, StudentAdmin)
admin.site.register(Teacher, TeacherAdmin)
admin.site.register(Group, GroupAdmin)
