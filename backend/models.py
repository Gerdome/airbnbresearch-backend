from django.db import models

class react360(models.Model):
    x_axis = models.IntegerField(default=0)
    y_axis = models.IntegerField(default=0)

class EventTracker(models.Model):
    item = models.CharField(max_length = 100)
    event = models.CharField(max_length = 100)

