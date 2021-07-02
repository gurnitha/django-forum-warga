# apps/boards/views.py

# Django modules
from django.shortcuts import render
from django.http import HttpResponse

# Django locals
from apps.boards.models import Board

# Create your views here.

# Home view
def home(request):
    boards = Board.objects.all()
    context = {'boards': boards}
    return render(request, 'home.html', context )