from django.db import models

# Create your models here.


class Student(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    birth_date = models.DateField()
    emails = models.EmailField()
    #TODO
    phone = models.CharField(max_length=16) #clean_ph TODO
    address = models.CharField(max_length=255, null=True, blank=True)