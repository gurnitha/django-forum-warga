# config/urls.py

# Django modules
from django.contrib import admin
from django.urls import path
from django.conf.urls import url

# Django locals
from apps.accounts import views as accounts_views
from apps.boards import views 

urlpatterns = [

    # Boards
    url(r'^$', views.home, name='home'),
    url(r'^signup/$', accounts_views.signup, name='signup'),
    url(r'^boards/(?P<pk>\d+)/$', views.board_topics, name='board_topics'),
    url(r'^boards/(?P<pk>\d+)/new/$', views.new_topic, name='new_topic'),
    # Admin dashboard
    path('admin/', admin.site.urls),
]
