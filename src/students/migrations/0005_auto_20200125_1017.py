# Generated by Django 2.2.9 on 2020-01-25 10:17

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ('students', '0004_auto_20200122_1221'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='group_id',
            new_name='groups',
        ),
    ]
