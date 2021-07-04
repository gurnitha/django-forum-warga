# apps/accounts/views.py

# Django modules
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login as auth_login
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.views.generic import UpdateView, ListView
from django.contrib.auth.models import User

# Django locals
from apps.accounts.forms import SignUpForm

# Create your views here.

# # Singup view
# def signup(request):
#     form = UserCreationForm()
#     return render(request, 'accounts/signup.html', {'form': form})

# -- replace by the codes bellow


# # Singup view
# from django.contrib.auth import login as auth_login
# from django.contrib.auth.forms import UserCreationForm
# from django.shortcuts import render, redirect

# def signup(request):
#     if request.method == 'POST':
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             user = form.save()
#             auth_login(request, user)
#             return redirect('home')
#     else:
#         form = UserCreationForm()
#     return render(request, 'accounts/signup.html', {'form': form})

# -- replace by the codes bellow

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


# Singup view
def signup(request):

    if request.method == 'POST':
        form = SignUpForm(request.POST)

        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('home')

    else:
        form = SignUpForm()

    return render(request, 'accounts/signup.html', {'form': form})

"""
Note:
It worked :)
"""   

# USERS
@method_decorator(login_required, name='dispatch')
class UserUpdateView(UpdateView):
    model = User
    fields = ('first_name', 'last_name', 'email', )
    template_name = 'accounts/my_account.html'
    success_url = reverse_lazy('my_account')

    def get_object(self):
        return self.request.user
