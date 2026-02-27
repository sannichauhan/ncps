from django.db import models

# Create your models here.
class Subject(models.Model):
    name = models.CharField(max_length=100)
    class_name = models.ForeignKey('school_classes.Class', on_delete=models.CASCADE)

    def __str__(self):
        return self.name