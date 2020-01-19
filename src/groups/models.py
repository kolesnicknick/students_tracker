from django.db import models

from faker import Faker


class Group(models.Model):
    group_name = models.CharField(max_length=20)
    senior = models.ForeignKey('students.Student',
                               null=True,
                               blank=True,
                               on_delete=models.CASCADE)
    curator = models.ForeignKey('teachers.Teacher',
                                null=True,
                                blank=True,
                                on_delete=models.CASCADE)

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
