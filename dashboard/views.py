from django.shortcuts import render
from . import views

# Create your views here.
def main_dashboard(request):
     return render(request, 'index.html')



