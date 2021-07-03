# apps/accounts/views.py

# Django modules
from django.shortcuts import render

# Django locals

# Create your views here.

# Singup view
def signup(request):
    return render(request, 'accounts/signup.html')

