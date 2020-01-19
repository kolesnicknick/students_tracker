from django.db import models

from faker import Faker


class Teacher(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    emails = models.EmailField()
    phone = models.CharField(max_length=16)
    assigned_group = models.CharField(max_length=16)

    def get_info(self):
        return f'{self.first_name} | {self.last_name} | {self.emails} | {self.phone}'

    @classmethod
    def gen_teacher(cls):
        fake = Faker()
        teacher = cls(
            first_name=fake.first_name(),
            last_name=fake.last_name(),
            emails=fake.email(),
            phone=fake.phone_number(),
            assigned_group='MD'
        )
        teacher.save()
        return teacher
