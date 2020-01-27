from django.db import models

from faker import Faker


class Student(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    birth_date = models.DateField()
    emails = models.EmailField(unique=True)
    phone = models.CharField(max_length=16)
    address = models.CharField(max_length=255, null=True, blank=True)
    groups = models.ForeignKey('groups.Group',
                               models.SET_NULL,
                               null=True,
                               blank=True)

    def get_info(self):
        return f'{self.first_name} | {self.last_name} | {self.birth_date} |' \
               f' {self.emails} | {self.phone} | {self.address}'

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

    @classmethod
    def generate_student(cls):
        fake = Faker()
        student = cls(
            first_name=fake.first_name(),
            last_name=fake.last_name(),
            birth_date=fake.date_of_birth(tzinfo=None, minimum_age=9, maximum_age=55),
            emails=fake.email(),
            phone=fake.phone_number(),
            address=fake.address()
        )
        student.save()
        return student
