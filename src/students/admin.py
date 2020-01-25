from django.contrib import admin

from groups.models import Group
from students.models import Student
from teachers.models import Teacher


# class UserProfileAdmin(.mod)

class StudentAdmin(admin.ModelAdmin):
    readonly_fields = ('emails', 'phone')
    last_display = ('id', 'first_name', 'last_name', 'emails', 'group')
    list_select_related = ['groups']

    def user_info(self, obj):
        pass

    def get_readonly_fields(self, request, obj=None):
        readonly_fields = super().get_readonly_fields(request, obj)
        if request.user.groups.filter('manager').exist():
            return readonly_fields + 'emails', 'phone',
        return readonly_fields


class TeacherAdmin(admin.ModelAdmin):
    pass


class StudentInline(admin.TabularInline):
    model = Student


class GroupAdmin(admin.ModelAdmin):
    inlines = [
        StudentInline
    ]


admin.site.register(Student, StudentAdmin)
admin.site.register(Teacher, TeacherAdmin)
admin.site.register(Group, GroupAdmin)
