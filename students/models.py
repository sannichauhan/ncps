from django.db import models

# Create your models here.


class Student(models.Model):
    name = models.CharField(max_length=100)
    roll_number = models.IntegerField()
    student_class = models.CharField(max_length=50)
    age = models.IntegerField()
    address = models.TextField()

    def __str__(self):
        return self.name
