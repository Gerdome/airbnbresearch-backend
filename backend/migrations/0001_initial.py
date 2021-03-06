# Generated by Django 3.1.3 on 2020-11-06 13:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EventTracker',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.CharField(default='20.05.2019', max_length=100)),
                ('item', models.CharField(max_length=100)),
                ('event', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='FullScreen',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.CharField(default='20.05.2019', max_length=100)),
                ('page', models.CharField(max_length=100)),
                ('event', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='GazeTracker',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('timestamp', models.CharField(default='01.11.2020', max_length=100)),
                ('gaze_target', models.CharField(max_length=100)),
                ('gaze_origin_x', models.CharField(max_length=100)),
                ('gaze_origin_y', models.CharField(max_length=100)),
                ('gaze_origin_z', models.CharField(max_length=100)),
                ('gaze_direction_x', models.CharField(max_length=100)),
                ('gaze_direction_y', models.CharField(max_length=100)),
                ('gaze_direction_z', models.CharField(max_length=100)),
                ('gaze_point_x', models.CharField(max_length=100)),
                ('gaze_point_y', models.CharField(max_length=100)),
                ('gaze_point_z', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='react360',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.CharField(default='20.05.2019', max_length=100)),
                ('x_axis', models.IntegerField(default=0)),
                ('y_axis', models.IntegerField(default=0)),
            ],
        ),
    ]
