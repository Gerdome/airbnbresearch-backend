from django.db import models


class react360(models.Model):
    x_axis = models.IntegerField(default=0)
    y_axis = models.IntegerField(default=0)

