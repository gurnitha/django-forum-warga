# apps/boards/views.py

# Django modules
from django.shortcuts import render
from django.http import HttpResponse
from django.http import Http404

# Django locals
from apps.boards.models import Board

# Create your views here.

# Home view
def home(request):
    boards = Board.objects.all()
    context = {'boards': boards}
    return render(request, 'home.html', context )


# # BoardTopic view
# def board_topics(request, pk):
#     board = Board.objects.get(pk=pk)
#     context = {'board': board}
#     return render(request, 'topics.html')

# -- replace by the codes bellow

# BoardTopic view
def board_topics(request, pk):
    try:
        board = Board.objects.get(pk=pk)
    except Board.DoesNotExist:
        raise Http404    
    context = {'board': board}
    return render(request, 'boards/topics.html', context)








