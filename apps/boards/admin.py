# apps/boards/admin.py

# Django modules
from django.contrib import admin

# Django locals
from apps.boards.models import Board, Topic, Post

# Register your models here.

admin.site.register(Board)
admin.site.register(Topic)
admin.site.register(Post)