from django.shortcuts import render

# Create your views here.
def main_dashboard(request):
     return render(request, 'index.html')

def user_login(request):
     return render(request, 'login.html')



