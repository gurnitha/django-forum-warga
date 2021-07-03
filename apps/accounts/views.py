# apps/accounts/views.py

# Django modules
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render

# Django locals

# Create your views here.

# Singup view
def signup(request):
    form = UserCreationForm()
    return render(request, 'accounts/signup.html', {'form': form})

