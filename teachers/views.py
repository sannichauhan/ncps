from django.shortcuts import render

# Create your views here.
def all_teacher(request):
     return render(request, 'all-teacher.html')

def teacher_details(request):
     return render(request, 'teacher-details.html')

def add_teacher(request):
     return render(request, 'add-teacher.html')

def teacher_payment(request):
     return render(request, 'teacher-payment.html')
