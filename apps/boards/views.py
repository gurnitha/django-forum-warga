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
    boards_names = list()

    for board in boards:
        boards_names.append(board.name)

    response_html = '<br>'.join(boards_names)

    return HttpResponse(response_html)