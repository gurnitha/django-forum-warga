# config/urls.py

# Django modules
from django.contrib import admin
from django.urls import path
from django.conf.urls import url

# Django locals
from apps.boards import views 

urlpatterns = [

    # Home page
    url(r'^$', views.home, name='home'),
    
    # Admin dashboard
    path('admin/', admin.site.urls),
]
