# apps/accounts/views.py

# Django modules
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render

# Django locals

# Create your views here.

# # Singup view
# def signup(request):
#     form = UserCreationForm()
#     return render(request, 'accounts/signup.html', {'form': form})

# -- replace by the codes bellow


# Singup view
from django.contrib.auth import login as auth_login
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'accounts/signup.html', {'form': form})

"""
A basic form processing with a small detail: the login 
function (renamed to auth_login to avoid clashing with 
the built-in login view).

If the form is valid, a User instance is created with 
the user = form.save(). The created user is then passed 
as an argument to the auth_login function, manually 
authenticating the user. After that, the view redirects 
the user to the homepage, keeping the flow of the application.

Let’s try it. First, submit some invalid data. 
Either an empty form, non-matching fields, or an 
existing username:

Now fill the form and submit it, check if the user 
is created and redirected to the homepage:

Note:
It worked :)
"""    