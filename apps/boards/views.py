# apps/boards/views.py

# Django modules
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.http import Http404
from django.db.models import Count
from django.views.generic import UpdateView, ListView
from django.utils import timezone
from django.utils.decorators import method_decorator
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Django locals
from apps.boards.forms import NewTopicForm, PostForm
from apps.boards.models import Board, Topic, Post

# Create your views here.

# # Home view 1
# def home(request):
#     boards = Board.objects.all()
#     context = {'boards': boards}
#     return render(request, 'boards/home.html', context )


# Home view 2 using GCBV
class BoardListView(ListView):
    model = Board
    context_object_name = 'boards'
    template_name = 'boards/home.html'


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


# # BoardTopic view 2
# def board_topics(request, pk):
#     board = get_object_or_404(Board, pk=pk)
#     topics = board.topics.order_by('-last_updated').annotate(replies=Count('posts') - 1)
#     return render(request, 'boards/topics.html', {'board': board, 'topics': topics})


# # BoardTopic view 3 add Pagination
# def board_topics(request, pk):
#     board = get_object_or_404(Board, pk=pk)
#     queryset = board.topics.order_by('-last_updated').annotate(replies=Count('posts') - 1)
#     page = request.GET.get('page', 1)

#     paginator = Paginator(queryset, 10)

#     try:
#         topics = paginator.page(page)
#     except PageNotAnInteger:
#         # fallback to the first page
#         topics = paginator.page(1)
#     except EmptyPage:
#         # probably the user tried to add a page number
#         # in the url, so we fallback to the last page
#         topics = paginator.page(paginator.num_pages)

#     return render(request, 'boards/topics.html', {'board': board, 'topics': topics})


# BoardTopic view 4 add Pagination (GCBV: TopicListView)
class TopicListView(ListView):
    model = Topic
    context_object_name = 'topics'
    template_name = 'boards/topics.html'
    paginate_by = 10

    def get_context_data(self, **kwargs):
        kwargs['board'] = self.board
        return super().get_context_data(**kwargs)

    def get_queryset(self):
        self.board = get_object_or_404(Board, pk=self.kwargs.get('pk'))
        queryset = self.board.topics.order_by('-last_updated').annotate(replies=Count('posts') - 1)
        return queryset



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


# # reply_topic 1
# @login_required
# def reply_topic(request, pk, topic_pk):

#     topic = get_object_or_404(Topic, board__pk=pk, pk=topic_pk)
    
#     if request.method == 'POST':
#         form = PostForm(request.POST)

#         if form.is_valid():
#             post = form.save(commit=False)
#             post.topic = topic
#             post.created_by = request.user
#             post.save()
#             return redirect('topic_posts', pk=pk, topic_pk=topic_pk)
    
#     else:
#         form = PostForm()

#     return render(request, 'boards/reply_topic.html', {'topic': topic, 'form': form})


# reply_topic 2
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

            topic.last_updated = timezone.now()  # <- here
            topic.save()                         # <- and here

            return redirect('topic_posts', pk=pk, topic_pk=topic_pk)
    else:
        form = PostForm()
    return render(request, 'boards/reply_topic.html', {'topic': topic, 'form': form})



# #GCBV: PostUpdateView 1
# class PostUpdateView(UpdateView):
#     model = Post
#     fields = ('message', )
#     template_name = 'boards/edit_post.html'
#     pk_url_kwarg = 'post_pk'
#     context_object_name = 'post'

#     def form_valid(self, form):
#         post = form.save(commit=False)
#         post.updated_by = self.request.user
#         post.updated_at = timezone.now()
#         post.save()
#         return redirect('topic_posts', pk=post.topic.board.pk, topic_pk=post.topic.pk)


# #GCBV: PostUpdateView 2
# @method_decorator(login_required, name='dispatch')
# class PostUpdateView(UpdateView):
#     model = Post
#     fields = ('message', )
#     template_name = 'boards/edit_post.html'
#     pk_url_kwarg = 'post_pk'
#     context_object_name = 'post'

#     def form_valid(self, form):
#         post = form.save(commit=False)
#         post.updated_by = self.request.user
#         post.updated_at = timezone.now()
#         post.save()
#         return redirect('topic_posts', pk=post.topic.board.pk, topic_pk=post.topic.pk)        


#GCBV: PostUpdateView 3
@method_decorator(login_required, name='dispatch')
class PostUpdateView(UpdateView):
    model = Post
    fields = ('message', )
    template_name = 'boards/edit_post.html'
    pk_url_kwarg = 'post_pk'
    context_object_name = 'post'

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(created_by=self.request.user)

    def form_valid(self, form):
        post = form.save(commit=False)
        post.updated_by = self.request.user
        post.updated_at = timezone.now()
        post.save()
        return redirect('topic_posts', pk=post.topic.board.pk, topic_pk=post.topic.pk)


# # PostListView 1
# class PostListView(ListView):
#     model = Post
#     context_object_name = 'posts'
#     template_name = 'boards/topic_posts.html'
#     paginate_by = 2

#     def get_context_data(self, **kwargs):
#         self.topic.views += 1
#         self.topic.save()
#         kwargs['topic'] = self.topic
#         return super().get_context_data(**kwargs)

#     def get_queryset(self):
#         self.topic = get_object_or_404(Topic, board__pk=self.kwargs.get('pk'), pk=self.kwargs.get('topic_pk'))
#         queryset = self.topic.posts.order_by('created_at')
#         return queryset


# PostListView 2
class PostListView(ListView):
    model = Post
    context_object_name = 'posts'
    template_name = 'boards/topic_posts.html'
    paginate_by = 2

    def get_context_data(self, **kwargs):

        session_key = 'viewed_topic_{}'.format(self.topic.pk)  # <-- here
        if not self.request.session.get(session_key, False):
            self.topic.views += 1
            self.topic.save()
            self.request.session[session_key] = True           # <-- until here

        kwargs['topic'] = self.topic
        return super().get_context_data(**kwargs)

    def get_queryset(self):
        self.topic = get_object_or_404(Topic, board__pk=self.kwargs.get('pk'), pk=self.kwargs.get('topic_pk'))
        queryset = self.topic.posts.order_by('created_at')
        return queryset



































