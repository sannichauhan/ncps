from django.shortcuts import render
from django import views

# Create your views here.



# Create your views here.
def all_parents(request):
     return render(request, 'all-parents.html')


def parents_details(request):
     return render(request, 'parents-details.html')

def add_parents(request):
     return render(request, 'add-parents.html')


