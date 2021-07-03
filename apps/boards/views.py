# apps/boards/views.py

# Django modules
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.http import Http404

# Django locals
from apps.boards.models import Board

# Create your views here.

# Home view
def home(request):
    boards = Board.objects.all()
    context = {'boards': boards}
    return render(request, 'boards/home.html', context )


# # BoardTopic view
# def board_topics(request, pk):
#     board = Board.objects.get(pk=pk)
#     context = {'board': board}
#     return render(request, 'topics.html')

# -- replace by the codes bellow

# # BoardTopic view
# def board_topics(request, pk):
#     try:
#         board = Board.objects.get(pk=pk)
#     except Board.DoesNotExist:
#         raise Http404    
#     context = {'board': board}
#     return render(request, 'boards/topics.html', context)

# -- replace by the codes bellow

# BoardTopic view
def board_topics(request, pk):
    board = get_object_or_404(Board, pk=pk) # <--- same result
    context = {'board': board}
    return render(request, 'boards/topics.html', context)


# NewTopic view
def new_topic(request, pk):
    board = get_object_or_404(Board, pk=pk)
    context = {'board':board}
    return render(request, 'boards/new_topic.html', context)



