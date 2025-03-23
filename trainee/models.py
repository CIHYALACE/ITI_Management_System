from django.db import models
from track.models import Tracks

# Create your models here.

class TraineeProfile(models.Model):
    trainee_id = models.AutoField(primary_key=True)
    trainee_first_name = models.CharField(max_length=100, null=False)
    trainee_last_name = models.CharField(max_length=100, null=False)
    trainee_email = models.EmailField(null=False)
    trainee_phone = models.IntegerField(null=False)
    trainee_address = models.CharField(null=False)
    trainee_image = models.ImageField()
    trainee_track = models.ForeignKey(to=Tracks, on_delete=models.SET_NULL, null=True)
    trainee_status = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.trainee_first_name} {self.trainee_last_name}"      

    @classmethod
    def getalltrainee(cls):
        return cls.objects.all()