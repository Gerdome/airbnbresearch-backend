from django.db import models

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

