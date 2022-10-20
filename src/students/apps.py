from django.apps import AppConfig


class StudentsConfig(AppConfig):
    name = 'students'

    def ready(self):
        from students.signals import pre_save_student
