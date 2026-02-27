from django.db import models


class Exam(models.Model):
    name = models.CharField(max_length=100)
    class_name = models.ForeignKey(
        'school_classes.Class',   # ✅ FIXED
        on_delete=models.CASCADE
    )
    date = models.DateField()

    def __str__(self):
        return self.name


class Result(models.Model):
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE)
    student = models.ForeignKey(
        'students.Student',
        on_delete=models.CASCADE,
        related_name='exam_results'   # ✅ prevent future conflict
    )
    marks = models.IntegerField()

    def __str__(self):
        return f"{self.student} - {self.exam}"