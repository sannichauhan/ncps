from django.db import models

# Create your models here.
class Vehicle(models.Model):
    vehicle_number = models.CharField(max_length=50)
    driver_name = models.CharField(max_length=100)
    route = models.CharField(max_length=200)