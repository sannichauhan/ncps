from django.urls import path
from . import views

urlpatterns = [
    path('all-teacher/', views.all_teacher, name="allteacher"),
    path('teacher-details/', views.teacher_details, name="teacherdetails"),
    path('add-teacher/', views.add_teacher, name="addteacher"),
    path('teacher-payment/', views.teacher_payment, name="teacherpayment"),
]