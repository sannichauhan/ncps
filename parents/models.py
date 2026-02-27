from django.db import models

# Create your models here.
class Parents(models.Model):
    father_name = models.CharField(max_length=100)
    mother_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    address = models.TextField(max_length=255, default="Not Available")

    def __str__(self):
        return self.father_name