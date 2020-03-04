from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Activity(models.Model):
    distance_km = models.DecimalField(max_digits=8,decimal_places=3)
    time_stamp =models.TimeField()
    activity_type = models.CharField(max_length=15)
    date = models.DateField()

    def __str__(self):
        return self.activity_type

    class Meta:
        verbose_name_plural = 'Activities'

class Totals(models.Model):
    user = models.CharField(max_length=15)
    distance_km = models.DecimalField(default=0,max_digits=8,decimal_places=3)
    time_total = models.IntegerField(default=0)
    walk_time = models.IntegerField(default=0)
    run_time = models.IntegerField(default=0)
    hike_time = models.IntegerField(default=0)
    bike_time = models.IntegerField(default=0)
    swim_time = models.IntegerField(default=0)
    other_time = models.IntegerField(default=0)

    class Meta:
        verbose_name_plural = 'Totals'
