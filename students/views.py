from django.shortcuts import render
from django import views

# Create your views here.
def all_student(request):
     return render(request, 'all-student.html')

def student_details(request):
     return render(request, 'student-details.html')

def admit_form(request):
     return render(request, 'admit-form.html')

def student_promotion(request):
     return render(request, 'student-promotion.html')
