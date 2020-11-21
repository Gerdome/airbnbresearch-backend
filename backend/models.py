from django.db import models

MALE, FEMALE = range(2)
GENDER = (
    (MALE, 'MALE'),
    (FEMALE, 'FEMALE')
)

CHINESE, SPANISH, ENGLISH, FRENCH, HINDI, ARABIC, RUSSIAN = range(7)
LANGUAGES = (
    (CHINESE, 'CHINESE'),
    (SPANISH, 'SPANISH'),
    (ENGLISH, 'ENGLISH'),
    (FRENCH, 'FRENCH'),
    (HINDI, 'HINDI'),
    (ARABIC, 'ARABIC'),
    (RUSSIAN, 'RUSSIAN'),
)

class Student(models.Model):
    full_name = models.CharField('Full Name', max_length=50)
    gender = models.PositiveSmallIntegerField('Gender', choices=GENDER, default=MALE)
    language = models.PositiveSmallIntegerField('Language', choices=LANGUAGES, default=ENGLISH)
    grades = models.CharField('Grades', max_length=2)

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = ('Student')

class react360(models.Model):
    timestamp = models.CharField(max_length = 100, default = '20.05.2019')
    x_axis = models.IntegerField(default=0)
    y_axis = models.IntegerField(default=0)

class EventTracker(models.Model):
    timestamp = models.CharField(max_length = 100, default = '20.05.2019')
    item = models.CharField(max_length = 100)
    event = models.CharField(max_length = 100)
    
class FullScreen(models.Model):
    timestamp =models.CharField(max_length = 100, default = '20.05.2019')
    page = models.CharField(max_length = 100)
    event = models.CharField(max_length = 100)

class GazeTracker(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    timestamp = models.CharField(max_length = 100, default = '01.11.2020')
    gaze_target = models.CharField(max_length = 100)

    gaze_origin_x = models.FloatField()
    gaze_origin_y = models.FloatField()
    gaze_origin_z = models.FloatField()

    gaze_direction_x = models.FloatField()
    gaze_direction_y = models.FloatField()
    gaze_direction_z = models.FloatField()

    gaze_point_x = models.FloatField()
    gaze_point_y = models.FloatField()
    gaze_point_z = models.FloatField()

    user_id = models.CharField(max_length=100)
    round_nr = models.CharField(max_length=100)
    subround_nr = models.CharField(max_length=100)

class VirtualObject(models.Model):
    vertices_x = models.CharField(max_length=10000)
    vertices_y = models.CharField(max_length=10000)
    vertices_z = models.CharField(max_length=10000)

class Calibration(models.Model):
    timestamp = models.CharField(max_length=1000)
    user_id = models.CharField(max_length=100)
    calibration_target = models.CharField(max_length = 100)

    target_point_x = models.FloatField()
    target_point_y = models.FloatField()
    target_point_z = models.FloatField()

    estimated_point_x = models.FloatField()
    estimated_point_y = models.FloatField()
    estimated_point_z = models.FloatField()

    gaze_origin_x = models.FloatField()
    gaze_origin_y = models.FloatField()
    gaze_origin_z = models.FloatField()

    gaze_direction_x = models.FloatField()
    gaze_direction_y = models.FloatField()
    gaze_direction_z = models.FloatField()

class Purchase(models.Model):
    city = models.CharField(max_length=50)
    customer_type = models.CharField(max_length=50)
    gender = models.CharField(max_length=50)
    unit_price = models.FloatField()
    quantity = models.IntegerField()
    product_line = models.CharField(max_length=50)
    tax = models.FloatField()
    total = models.FloatField()
    date = models.DateField()
    time = models.TimeField()
    payment	= models.CharField(max_length=50)
    cogs = models.FloatField()
    profit = models.FloatField()
    rating  = models.FloatField()