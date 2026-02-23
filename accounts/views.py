from django.shortcuts import render

# Create your views here.
def all_fees(request):
     return render(request, 'all-fees.html')