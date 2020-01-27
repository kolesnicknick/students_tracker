from django.conf import settings
from django.core.mail import send_mail
from django.forms import ModelForm, Form, EmailField, CharField, ValidationError

from .models import Student


class StudentsAddForm(ModelForm):
    class Meta:
        model = Student
        fields = '__all__'


class StudentsAdminForm(ModelForm):
    class Meta:
        model = Student
        fields = '__all__'
        exclude = ['id']

    def clean_emails(self):
        email = self.cleaned_data['emails'].lower()
        if Student.objects.filter(emails__iexact=email).exists():
            raise ValidationError(f'Email {email} is already used')
        return email


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
