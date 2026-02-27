from django.shortcuts import get_object_or_404, render, redirect
from .models import Student
from .form import StudentForm
from django.contrib import messages

# Create your views here.
def all_student(request):
     return render(request, 'all-student.html')

def student_details(request):
     return render(request, 'student-details.html')

# def admit_form(request):     
#     try:
#         student = Student.objects.get()
#         form = StudentForm(instance=student)
#     except Student.DoesNotExist:
#         form = StudentForm()    
#     return render(request, 'admit-form.html', {'form': form})

def admit_form(request):
    if request.method == "POST":
        form = StudentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('all-student.html')
    else:
        form = StudentForm()
    return render(request, "admit-form.html", {"form": form})

def student_register(request):
    message=''
    if request.method == "POST":      
      form = StudentForm(request.POST)
      if form.is_valid():
          form.save()
          message="Form save successfully!"
          messages.success(request, message)
          return redirect(request.path)          
      else:
          messages.error(request, form.errors,)
          return redirect(request.path)
    else:
        message=''
        form = StudentForm()
        all_info = Student.objects.all()
        return render(request, 'admit-form.html', {'form':form, 'message':message, 'all_info':all_info})

def student_promotion(request):
     return render(request, 'student-promotion.html')
