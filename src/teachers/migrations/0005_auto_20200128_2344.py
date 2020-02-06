# Generated by Django 2.2.9 on 2020-01-28 23:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teachers', '0004_auto_20200125_1017'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacher',
            name='degree',
            field=models.PositiveSmallIntegerField(choices=[(1, 'A.S.'), (2, 'M.S.'), (3, 'Ph.D.'), (4, 'J.D.'), (5, 'M.D.')], default=1),
        ),
    ]