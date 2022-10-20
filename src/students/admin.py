from django.contrib import admin

from students.forms import StudentsAdminForm
from students.models import Student


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


admin.site.register(Student, StudentAdmin)
