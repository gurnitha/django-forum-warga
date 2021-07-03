# apps/boards/views.py

# Django modules
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.http import Http404
from django.db.models import Count

# Django locals
from apps.boards.forms import NewTopicForm, PostForm
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

# # BoardTopic view 1
# def board_topics(request, pk):
#     board = get_object_or_404(Board, pk=pk) # <--- same result
#     context = {'board': board}
#     return render(request, 'boards/topics.html', context)


# BoardTopic view 2
def board_topics(request, pk):
    board = get_object_or_404(Board, pk=pk)
    topics = board.topics.order_by('-last_updated').annotate(replies=Count('posts') - 1)
    return render(request, 'boards/topics.html', {'board': board, 'topics': topics})


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


# # NewTopic view
# @login_required
# def new_topic(request, pk):
#     board = get_object_or_404(Board, pk=pk)
#     user = User.objects.first()  # TODO: get the currently logged in user
    
#     if request.method == 'POST':
#         form = NewTopicForm(request.POST)
        
#         if form.is_valid():
#             topic = form.save(commit=False)
#             topic.board = board
#             topic.starter = user
#             topic.save()
#             post = Post.objects.create(
#                 message=form.cleaned_data.get('message'),
#                 topic=topic,
#                 created_by=user
#             )

#             return redirect('board_topics', pk=board.pk)  # TODO: redirect to the created topic page
    
#     else:
#         form = NewTopicForm()

#     context = {'board':board, 'form':form}
#     return render(request, 'boards/new_topic.html', context)  

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

# -- replace by the codes bellow

# NewTopic view
@login_required
def new_topic(request, pk):
    board = get_object_or_404(Board, pk=pk)

    if request.method == 'POST':
        form = NewTopicForm(request.POST)

        if form.is_valid():
            topic = form.save(commit=False)
            topic.board = board
            topic.starter = request.user
            topic.save()
            Post.objects.create(
                message=form.cleaned_data.get('message'),
                topic=topic,
                created_by=request.user
            )
            # return redirect('board_topics', pk=board.pk)  # TODO: redirect to the created topic page
            return redirect('topic_posts', pk=pk, topic_pk=topic.pk)  # <- here    
    else:
        form = NewTopicForm()

    return render(request, 'boards/new_topic.html', {'board': board, 'form': form})


"""
Note with this codes:
1. New user: Victor
2. Victor logged in
3. He made a topic on Python
4. His topic and his name (as starter) appear on Python topic
5. Similarly if he made something on Django topic,
   the same thing happen
6. See bellow
================================================================================

Boards / Python

-----------
|New topic|
-----------

Topic                   Starter     Replies     Views   Last Update
--------------------------------------------------------------------------------
Victor proposal         Victor      0           0       July 3, 2021, 9:35 a.m.
Python is great         ing         0           0       July 3, 2021, 9:42 a.m.

================================================================================

Boards / Django

-----------
|New topic|
-----------

Topic                   Starter     Replies     Views   Last Update
--------------------------------------------------------------------------------
Hallo every one         ing         0           0       July 3, 2021, 1:07 a.m.
After protecting view   ing         0           0       July 3, 2021, 9:33 a.m.
Victor on Django        Victor      0           0       July 3, 2021, 9:36 a.m.   
================================================================================
"""


# # TopicPosts view 1
# def topic_posts(request, pk, topic_pk):
#     topic = get_object_or_404(Topic, board__pk=pk, pk=topic_pk)
#     return render(request, 'boards/topic_posts.html', {'topic': topic})

# # http://127.0.0.1:8000/boards/1/topics/1/

# # Boards /Django / Hallo every one


# TopicPosts view 2
def topic_posts(request, pk, topic_pk):
    topic = get_object_or_404(Topic, board__pk=pk, pk=topic_pk)
    topic.views += 1
    topic.save()
    return render(request, 'boards/topic_posts.html', {'topic': topic})


@login_required
def reply_topic(request, pk, topic_pk):

    topic = get_object_or_404(Topic, board__pk=pk, pk=topic_pk)
    
    if request.method == 'POST':
        form = PostForm(request.POST)

        if form.is_valid():
            post = form.save(commit=False)
            post.topic = topic
            post.created_by = request.user
            post.save()
            return redirect('topic_posts', pk=pk, topic_pk=topic_pk)
    
    else:
        form = PostForm()

    return render(request, 'boards/reply_topic.html', {'topic': topic, 'form': form})