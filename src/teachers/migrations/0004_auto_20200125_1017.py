# Generated by Django 2.2.9 on 2020-01-25 10:17

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('teachers', '0003_remove_teacher_assigned_group'),
    ]

    operations = [
        migrations.RenameField(
            model_name='teacher',
            old_name='emails',
            new_name='email',
        ),
        migrations.AddField(
            model_name='teacher',
            name='degree',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]