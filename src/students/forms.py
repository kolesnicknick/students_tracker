from django.conf import settings
from django.core.mail import send_mail
from django.forms import ModelForm, Form, EmailField, CharField, ValidationError

from .models import Student


class StudentsBase(ModelForm):
    def clean_emails(self):
        email = self.cleaned_data['emails'].lower()
        emails_exists = Student.objects \
            .filter(emails__iexact=email)
        try:
            emails_exists = emails_exists.exclude(id=self.instance.id)
        except Exception:
            print('no student found')

        print(emails_exists.query)
        if emails_exists.exists():
            raise ValidationError(f'{email} is already used!')
        return email

    def clean_phone(self):
        phone = self.cleaned_data['phone']

        phone_exists = Student.objects \
            .filter(phone__iexact=phone)
        try:
            phone_exists = phone_exists.exclude(id=self.instance.id)
        except Exception:
            print('no student found')

        return phone


class StudentsAddForm(StudentsBase):
    class Meta:
        model = Student
        fields = '__all__'


class StudentsAdminForm(StudentsBase):
    class Meta:
        model = Student
        fields = '__all__'
        exclude = ['id']


class ContactForm(Form):
    email = EmailField()
    subject = CharField()
    text = CharField()

    def save(self):
        data = self.cleaned_data
        subject = data['subject']
        message = data['text']
        email_from = data['email']
        recipient_list = [settings.EMAIL_HOST_USER]
        send_mail(subject, message, email_from, recipient_list)
