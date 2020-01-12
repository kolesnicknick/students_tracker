from django.db import models

# Create your models here.


class Student(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    birth_date = models.DateField()
    emails = models.EmailField()
    phone = models.CharField(max_length=16)
    address = models.CharField(max_length=255, null=True, blank=True)

    def get_info(self):
        return f'{self.first_name} {self.last_name} {self.birth_date} {self.emails} {self.phone} {self.address}'

    @classmethod
    def generate_student(cls):
        fake = Faker()
        student = cls(
            first_name=fake.first_name(),
            last_name=fake.last_name(),
            birth_date=fake.datetime.now(),
            emails=fake.email(),
            phone=fake.phone_number(),
            address=fake.address()
        )
        student.save()
        return student
