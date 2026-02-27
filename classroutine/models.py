from django.db import models

# Create your models here.

class Classroutine(models.Model):
    class_name = models.ForeignKey('school_classes.Class', on_delete=models.CASCADE)
    subject = models.ForeignKey('subject.Subject', on_delete=models.CASCADE)
    teacher = models.ForeignKey('teachers.Teacher', on_delete=models.CASCADE)
    day = models.CharField(max_length=20)
    start_time = models.TimeField()
    end_time = models.TimeField()
