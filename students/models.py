from django.db import models
from django.utils import timezone
from django.db import models


# Create your models here.
class Student(models.Model):

    GENDER_CHOICES = [
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Others', 'Others'),
    ]

    RELIGION_CHOICES = [
        ('Hindu', 'Hindu'),
        ('Islam', 'Islam'),
        ('Christian', 'Christian'),
        ('Buddhist', 'Buddhist'),
        ('Others', 'Others'),
    ]

    CLASS_CHOICES = [
        ('Play', 'Play'),
        ('Nursery', 'Nursery'),
        ('One', 'One'),
        ('Two', 'Two'),
        ('Three', 'Three'),
        ('Four', 'Four'),
        ('Five', 'Five'),
        ('Six', 'Six'),
        ('Seven', 'Seven'),
        ('Eight', 'Eight'),
        ('Nine', 'Nine'),
        ('Ten', 'Ten'),
        ('Eleven', 'Eleven'),
        ('Twelve', 'Twelve'),
    ]

    # ================= BASIC DETAILS =================
    date_of_application = models.DateField(
        default=timezone.now
    )
    name = models.CharField(max_length=100)
    date_of_birth = models.DateField(
        default=timezone.now
    )

    admission_class = models.CharField(
        max_length=20,
        choices=CLASS_CHOICES,
        default='Play'  # prevents migration error
    )

    gender = models.CharField(max_length=10, choices=GENDER_CHOICES, default="Male")
    religion = models.CharField(max_length=20, choices=RELIGION_CHOICES, default="Hindu")
    caste = models.CharField(max_length=50)

    # ================= PARENTS DETAILS =================
    mother_name = models.CharField(max_length=100, blank=True, null=True)
    father_name = models.CharField(max_length=100, blank=True, null=True)
    mother_occupation = models.CharField(max_length=100, blank=True, null=True)
    father_occupation = models.CharField(max_length=100, blank=True, null=True)

    # ================= CONTACT DETAILS =================
    contact_number = models.CharField(max_length=15, default="")
    permanent_address = models.TextField(default="")
    local_address = models.TextField(blank=True, null=True)
    pin_code = models.CharField(max_length=6, blank=True, null=True)
    district = models.CharField(max_length=100, blank=True, null=True)
    nationality = models.CharField(max_length=50, default="Indian")

    # ================= OTHER DETAILS =================
    adhaar_number = models.CharField(
        max_length=12,
        blank=True,
        null=True,
        unique=True
    )

    residence_in_up = models.CharField(max_length=100, blank=True, null=True)
    last_institution = models.CharField(max_length=200, blank=True, null=True)

    # ================= PHOTO =================
    student_photo = models.ImageField(
        upload_to='students/',
        blank=True,
        null=True
    )

    # ================= SYSTEM FIELDS =================
    created_at = models.DateTimeField(
        default=timezone.now
    )

    def __str__(self):
        return f"{self.name} ({self.admission_class})"
    
class Attendance(models.Model):
    student = models.ForeignKey('students.Student', on_delete=models.CASCADE)
    date = models.DateField()
    status = models.CharField(max_length=10, choices=[
        ('Present', 'Present'),
        ('Absent', 'Absent'),
    ])




