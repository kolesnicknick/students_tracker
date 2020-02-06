from celery import task, shared_task
from time import sleep

from django.core.mail import send_mail


@shared_task
def add(a, b):
    print('CELERY ADD WORKS')
    print(a + b)
    sleep(10)
    return a + b

@shared_task
def send_mail_async(subject, message, email_from, recipient_list):
    send_mail(subject, message, email_from, recipient_list)

