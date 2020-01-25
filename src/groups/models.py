from django.db import models

from faker import Faker


class Group(models.Model):
    group_name = models.CharField(max_length=20)
    senior = models.ForeignKey('students.Student',
                               models.SET_NULL,
                               null=True,
                               blank=True, )
    curator = models.ForeignKey('teachers.Teacher',
                                models.SET_NULL,
                                null=True,
                                blank=True,
                                )

    def get_info(self):
        return f'{self.group_name}'

    def __str__(self):
        return self.get_info()

    @classmethod
    def gen_group(cls):
        fake = Faker()
        group = cls(
            group_name=fake.license_plate(),
        )
        group.save()
        return group
