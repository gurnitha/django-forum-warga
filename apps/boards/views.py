# apps/boards/views.py

# Django modules
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.http import Http404

# Django locals
from apps.boards.forms import NewTopicForm
from apps.boards.models import Board, Topic, Post

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


# # NewTopic view
# def new_topic(request, pk):
#     board = get_object_or_404(Board, pk=pk)
#     context = {'board':board}
#     return render(request, 'boards/new_topic.html', context)

# -- replace by the codes bellow


# # NewTopic view
# def new_topic(request, pk):
#     board = get_object_or_404(Board, pk=pk)

#     if request.method == 'POST':
#         subject = request.POST['subject']
#         message = request.POST['message']

#         user = User.objects.first()  # TODO: get the currently logged in user

#         topic = Topic.objects.create(
#             subject=subject,
#             board=board,
#             starter=user
#         )

#         post = Post.objects.create(
#             message=message,
#             topic=topic,
#             created_by=user
#         )

#         return redirect('board_topics', pk=board.pk)  # TODO: redirect to the created topic page
#     context = {'board':board}
#     return render(request, 'boards/new_topic.html', context)

# -- replace by the codes bellow


# NewTopic view
@login_required
def new_topic(request, pk):
    board = get_object_or_404(Board, pk=pk)
    user = User.objects.first()  # TODO: get the currently logged in user
    
    if request.method == 'POST':
        form = NewTopicForm(request.POST)
        
        if form.is_valid():
            topic = form.save(commit=False)
            topic.board = board
            topic.starter = user
            topic.save()
            post = Post.objects.create(
                message=form.cleaned_data.get('message'),
                topic=topic,
                created_by=user
            )

            return redirect('board_topics', pk=board.pk)  # TODO: redirect to the created topic page
    
    else:
        form = NewTopicForm()

    context = {'board':board, 'form':form}
    return render(request, 'boards/new_topic.html', context)  

"""
First we check if the request is a POST or a GET. If the request came 
from a POST, it means the user is submitting some data to the server. 
So we instantiate a form instance passing the POST data to 
the form: form = NewTopicForm(request.POST).
Then, we ask Django to verify the data, check if the form is valid 
if we can save it in the database: if form.is_valid():. If the form 
was valid, we proceed to save the data in the database using form.save(). 
The save() method returns an instance of the Model saved into the database. 
So, since this is a Topic form, it will return the Topic that
was created: topic = form.save(). After that, the common path 
is to redirect the user somewhere else, both to avoid the user 
re-submitting the form by pressing F5 and also to keep the flow 
of the application.
Now, if the data was invalid, Django will add a list of errors to the form. 
After that, the view does nothing and returns in the last 
statement: return render(request, 'new_topic.html', {'form': form}). 
That means we have to update the new_topic.html to display errors properly.
If the request was a GET, we just initialize a new and empty 
form using form = NewTopicForm().

Then, we ask Django to verify the data, check if the form is valid if we 
can save it in the database: if form.is_valid():. If the form was valid, 
we proceed to save the data in the database using form.save(). The save()
method returns an instance of the Model saved into the database. 
So, since this is a Topic form, it will return the Topic that was 
created: topic = form.save(). After that, the common path is to redirect 
the user somewhere else, both to avoid the user re-submitting the form 
by pressing F5 and also to keep the flow of the application.

Now, if the data was invalid, Django will add a list of errors to the form. 
After that, the view does nothing and returns in the last 
statement: return render(request, 'new_topic.html', {'form': form}). 
That means we have to update the new_topic.html to display errors properly.

If the request was a GET, we just initialize a new and 
empty form using form = NewTopicForm().

"""