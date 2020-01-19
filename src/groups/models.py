# Create your models here.
from django.db import models

from faker import Faker


class Group(models.Model):
    group_name = models.CharField(max_length=20)

    def get_info(self):
        return f'{self.group_name}'

    @classmethod
    def gen_group(cls):
        fake = Faker()
        group = cls(
            group_name=fake.license_plate(),
        )
        group.save()
        return group
