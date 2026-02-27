from django.db import models

# Create your models here.
class Room(models.Model):
    room_number = models.CharField(max_length=20)
    capacity = models.IntegerField()

class HostelStudent(models.Model):
    student = models.ForeignKey('students.Student', on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)