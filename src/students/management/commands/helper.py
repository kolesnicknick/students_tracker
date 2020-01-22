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
        print(len(students))

        # Create 10 teachers wo group
        teachers = [Teacher.gen_teacher() for i in range(10)]
        print(len(teachers))

        # Create 10 groups wo teacher and senior
        groups = [Group.gen_group() for i in range(10)]

        # Update students with random Group
        for student in students:
            student.group_id = random.choice(groups)
            print(student.group_id)
            student.save()

        # Add for Group senior FROM THE GROUP and curator - random teacher
        for group in groups:
            while group.senior is None:
                student = random.choice(students)
                if student.group_id.id == group.id:
                    group.senior = student
                else:
                    print(f'student {student.group_id} not in group {group.id}')
            group.curator = random.choice(teachers)
            group.save()
            print(group.get_info())



