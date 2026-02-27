from django.urls import path
from . import views

urlpatterns = [
    path('', views.main_dashboard, name='dashboard'),
    path('login/', views.user_login, name='login'),
]