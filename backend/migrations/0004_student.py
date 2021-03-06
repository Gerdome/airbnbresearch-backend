# Generated by Django 3.1.3 on 2020-11-06 16:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0003_gazetracker_created_at'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=50, verbose_name='Full Name')),
                ('gender', models.PositiveSmallIntegerField(choices=[(0, 'MALE'), (1, 'FEMALE')], default=0, verbose_name='Gender')),
                ('language', models.PositiveSmallIntegerField(choices=[(0, 'CHINESE'), (1, 'SPANISH'), (2, 'ENGLISH'), (3, 'FRENCH'), (4, 'HINDI'), (5, 'ARABIC'), (6, 'RUSSIAN')], default=2, verbose_name='Language')),
                ('grades', models.CharField(max_length=2, verbose_name='Grades')),
            ],
            options={
                'verbose_name': 'Student',
            },
        ),
    ]
