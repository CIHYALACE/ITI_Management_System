from django.db import models
from track.models import Tracks

# Create your models here.


class Courses(models.Model):
    course_id = models.AutoField(primary_key=True)
    course_name = models.CharField(max_length=100)
    course_duration = models.CharField(max_length=100)
    course_fee = models.CharField(max_length=100)
    course_trainer = models.CharField(max_length=100)
    course_start_date = models.DateField()
    course_end_date = models.DateField()
    course_track = models.ForeignKey(to=Tracks, on_delete=models.SET_NULL, null=True)
    course_status = models.BooleanField(default=True)


def __str__(self):
    return f"{self.course_name} - {self.track.name if self.track else 'No Track'}"
    