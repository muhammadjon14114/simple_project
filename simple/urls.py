# simple/urls.py
from django.urls import path
from .views import CustomLoginView, RegisterView, DashboardView
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),
    path('register/', RegisterView.as_view(), name='register'),
    path('dashboard/', DashboardView.as_view(), name='dashboard'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
]
