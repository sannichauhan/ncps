from django.urls import path
from . import views

urlpatterns = [
    path('all-student/', views.all_student, name="allstudents"),
    path('student-details/', views.student_details, name="studentdetails"),
    path('admit-form/', views.admit_form, name="admitform"),
    path('admit-form/<int:id>/', views.admit_form, name="update_student"),
    path('student-promotion/', views.student_promotion, name="studentpromotion"),
]