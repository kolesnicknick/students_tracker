from django.core.management.base import BaseCommand
from faker.generator import random

from groups.models import Group
from students.models import Student


class Command(BaseCommand):
    help = 'Generate random students'

    def add_arguments(self, parser):
        parser.add_argument(
            '--number',
            help='Delete poll instead of closing it'
        )

    def handle(self, *args, **options):
        Group.objects.all().delete()
        Student.objects.all().delete()

        groups = [Group.objects.create(group_name=f'name_{i}')
                  for i in range(10)]

        for i in range(100):
            student = Student.generate_student()
            student.group_id = random.choice(groups)
            student.save()
