from django.core.exceptions import ValidationError
from django.forms import ModelForm

from teachers.models import Teacher


class TeacherFormBase(ModelForm):
    def clean_email(self):
        email = self.cleaned_data['email'].lower()
        email_exists = Teacher.objects \
            .filter(email__iexact=email)
        try:
            email_exists = email_exists.exclude(id=self.instance.id)
        except Exception:
            print('no teacher found')
        if email_exists.exists():
            raise ValidationError(f'{email} is already used!')
        return email

    def clean_phone(self):
        phone = self.cleaned_data['phone']

        phone_exists = Teacher.objects \
            .filter(phone__iexact=phone)
        try:
            phone_exists = phone_exists.exclude(id=self.instance.id)
        except Exception:
            print('no student found')
        if phone_exists.exists():
            raise ValidationError(f'{phone} is already used!')
        return phone


class TeacherAddForm(TeacherFormBase):
    class Meta:
        model = Teacher
        fields = '__all__'


class TeacherAdminForm(TeacherFormBase):
    class Meta:
        model = Teacher
        fields = '__all__'
        exclude = ['id']
