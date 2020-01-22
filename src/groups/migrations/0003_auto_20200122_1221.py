# Generated by Django 2.2.9 on 2020-01-22 12:21

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('groups', '0002_auto_20200119_1507'),
    ]

    operations = [
        migrations.AlterField(
            model_name='group',
            name='curator',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL,
                                    to='teachers.Teacher'),
        ),
        migrations.AlterField(
            model_name='group',
            name='senior',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL,
                                    to='students.Student'),
        ),
    ]