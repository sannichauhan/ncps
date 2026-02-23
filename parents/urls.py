from django.urls import path
from . import views

urlpatterns = [
    path('all-parents/', views.all_parents, name="parents"),
    path('parents-details/', views.parents_details, name="parentsdetails"),
    path('add-parents/', views.add_parents, name="addparents"),
]