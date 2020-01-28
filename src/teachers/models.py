from django.db import models
from faker import Faker
from faker.generator import random


class Teacher(models.Model):
    DEGREE = (
        (1, 'A.S.'), (2, 'M.S.'), (3, 'Ph.D.'), (4, 'J.D.'), (5, 'M.D.')
    )

    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.EmailField()
    degree = models.PositiveSmallIntegerField(choices=DEGREE, default=1)
    phone = models.CharField(max_length=16)

    def get_info(self):
        return f'{self.first_name} | {self.last_name} | {self.email} | {self.phone}'

    def __str__(self):
        return f'{self.degree} {self.first_name} {self.last_name}'

    @classmethod
    def gen_teacher(cls):
        fake = Faker()
        teacher = cls(
            first_name=fake.first_name(),
            last_name=fake.last_name(),
            degree=random.randint(1, 5),
            email=fake.email(),
            phone=fake.phone_number(),
        )
        teacher.save()
        return teacher
