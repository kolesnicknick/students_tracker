from django.db import models

# Create your models here.
from django.db.models import DateTimeField, IntegerField, CharField


class Log(models.Model):
    path = CharField(max_length=20)
    method = CharField(max_length=20)
    user_id = IntegerField(max_length=20)
    created = DateTimeField(auto_now=True)

    def get_info(self):
        return f'{self.path} | {self.method} | {self.user_id} |' \
               f' {self.created}'

    def __str__(self):
        return f'{self.created} : {self.method} {self.path} by user: {self.user_id}'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

    @classmethod
    def generate_log(cls, **kwargs):
        log = cls(
            path=kwargs['name'],
            method=kwargs['method'],
            user_id=kwargs['user_id'],
            created=kwargs['time']
        )
        log.save()
        return log
