from django.db import models

# Create your models here.
# note you can edit the models onley when there is no dependecies on it.

class Tracks(models.Model):
    track_id = models.AutoField(primary_key=True)
    track_name = models.CharField(max_length=50 , null=True, unique=True)
    track_duration =models.IntegerField(null=True)
    track_supervisor = models.CharField(max_length=50 , null=True)
    track_start_date = models.DateField(null=True)
    track_end_date = models.DateField(null=True)
    track_status = models.BooleanField(default=True)

    def __str__(self):
        return self.track_name