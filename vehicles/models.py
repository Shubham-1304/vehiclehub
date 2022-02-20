from email.policy import default
from django.db import models

class Vehicle(models.Model):
    name=models.CharField(max_length=50)
    camera1=models.BooleanField(default=False)
    camera2=models.BooleanField(default=False)
    speed=models.FloatField(default=0.0)
    averageSpeed=models.FloatField(default=0.0)
    temperature=models.FloatField(default=0.0)
    fuelLevel=models.FloatField(default=0.0)
    engineStatus=models.BooleanField(default=False)
    maps=models.ImageField(default=None)

    def __str__(self) -> str:
        return self.name


