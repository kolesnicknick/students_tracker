from django.db.models.signals import pre_save
from django.dispatch import receiver

from students.models import Student


@receiver(pre_save, sender=Student)
def pre_save_student(sender, instance, **kwargs):
    instance.emails = instance.emails.lower()
    instance.last_name = instance.last_name.title()
    instance.first_name = instance.first_name.title()
    instance.phone = "".join(x for x in instance.phone if x.isdigit())
