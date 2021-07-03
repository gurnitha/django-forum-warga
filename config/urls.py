# config/urls.py

# Django modules
from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from django.contrib.auth import views as auth_views

# Django locals
from apps.accounts import views as accounts_views
from apps.boards import views 

urlpatterns = [

    # Boards
    url(r'^$', views.home, name='home'),
    url(r'^signup/$', accounts_views.signup, name='signup'),
    url(r'^login/$', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'),
    url(r'^logout/$', auth_views.LogoutView.as_view(), name='logout'),
    url(r'^boards/(?P<pk>\d+)/$', views.board_topics, name='board_topics'),
    url(r'^boards/(?P<pk>\d+)/new/$', views.new_topic, name='new_topic'),
    # Admin dashboard
    path('admin/', admin.site.urls),
]
