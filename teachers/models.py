from django.db import models
from django.utils import timezone

# Create your models here.
class Teacher(models.Model):
    name = models.CharField(max_length=100)
    subject = models.ForeignKey('subject.Subject', on_delete=models.CASCADE)
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    joining_date = models.DateField(default=timezone.now)

    def __str__(self):
        return self.name
