from django.core.management.base import BaseCommand
from faker.generator import random

from groups.models import Group
from students.models import Student
from teachers.models import Teacher


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
        Teacher.objects.all().delete()

        # Create 100 students wo group/teacher
        students = [Student.generate_student() for i in range(100)]

        # Create 10 teachers wo group
        teachers = [Teacher.generate_teacher() for i in range(10)]

        # Create 10 groups with random senior/curator
        groups = [Group.generate_group() for i in range(10)]
        for group in groups:
            group.senior = random.choice(students)
            group.curator = random.choice(teachers)

        # Update students with random Group
        for student in students:
            student.group_id = random.choice(groups)
