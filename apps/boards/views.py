# apps/boards/views.py

# Django modules
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

# Home view
def home(request):
    return HttpResponse('Hello, World!')