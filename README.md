# DJANO FORUM WARGA
Membuat Aplikasi Forum Warga menggunakan Django v3.2

### -------------------------
### Part 1 - Getting Started
### -------------------------


#### 1.1.1 Creating Remote Repository

        modified:   .gitignore
        modified:   README.md

#### 1.2.2 Installing Virtualenv

        E:\workspace\django\ForumWarga\django-forum-warga (main)
        λ python -m venv venv3932

        modified:   README.md

#### 1.3.3 Installing Django 3.2

        E:\workspace\django\ForumWarga\django-forum-warga (main)
        λ venv3932\scripts\activate

        E:\workspace\django\ForumWarga\django-forum-warga (main)
        (venv3932) λ python -m pip install django==3.2

        E:\workspace\django\ForumWarga\django-forum-warga (main)
        (venv3932) λ python -m pip install --upgrade pip

        modified:   README.md

#### 1.4.4 Starting a New Project 'config'

        E:\workspace\django\ForumWarga\django-forum-warga (main)
        (venv3932) λ django-admin startproject config .

        .
        ├── README.md
        ├── config
        │   ├── __init__.py
        │   ├── asgi.py
        │   ├── settings.py
        │   ├── urls.py
        │   └── wsgi.py
        ├── manage.py
        └── venv3932
            ├── Include
            ├── Lib
            ├── Scripts
            └── pyvenv.cfg

#### 1.5.5 Django Apps

       .
       ├── README.md
       ├── apps
       │   └── boards
       │       ├── __init__.py
       │       ├── admin.py
       │       ├── apps.py
       │       ├── migrations
       │       ├── models.py
       │       ├── tests.py
       │       └── views.py
       ├── config
       │   ├── __init__.py
       │   ├── asgi.py
       │   ├── settings.py
       │   ├── urls.py
       │   └── wsgi.py
       ├── manage.py
       └── venv3932
            ├── Include
            ├── Lib
            ├── Scripts
            └── pyvenv.cfg

        E:\workspace\django\ForumWarga\django-forum-warga (main)
        (venv3932) λ python manage.py check
        System check identified no issues (0 silenced).

#### Modified readme.md

#### 1.6.6 Hello, World!

        modified:   README.md
        modified:   apps/boards/views.py
        modified:   config/urls.py

#### 1.1.7 Conclusions

        Conclusions
        
        That was the first part of this tutorial series. In this tutorial, we learned how to install the latest Python version and how to setup the development environment. We also had an introduction to virtual environments and started our very first Django project and already created our initial app.

        modified:   README.md


### ------------------------------------------------------
### Part 2 - Fundamentals: Database, Model, View, Template
### ------------------------------------------------------


#### 2.1.8 Create postgres database

        hp=# CREATE DATABASE django_forum_warga;
        CREATE DATABASE

        modified:   .gitignore
        modified:   README.md

#### 2.2.9 Install PostgreSQL driver

       E:\workspace\django\ForumWarga\django-forum-warga (main)
       (venv3932) λ python -m pip install psycopg2-binary==2.8.6

       modified:   README.md

#### 2.3.10 Install django environ

       E:\workspace\django\ForumWarga\django-forum-warga (main)
       (venv3932) λ pip install django-environ

        modified:   README.md

#### 2.4.11 Create .env file and setup environ

       E:\workspace\django\ForumWarga\django-forum-warga (main)
       (venv3932) λ touch config\.env

        modified:   README.md

#### 2.5.12 Use environ in settings

        E:\workspace\django\ForumWarga\django-forum-warga (main)
        (venv3932) λ python manage.py check
        System check identified no issues (0 silenced).

        modified:   README.md
        modified:   config/settings.py

#### 2.6.13 Models: Create Board, Topic and Post models

        E:\workspace\django\ForumWarga\django-forum-warga (main)
        (venv3932) λ python manage.py check
        System check identified no issues (0 silenced).

        modified:   README.md
        modified:   apps/boards/models.py

#### 2.7.14 Migrating the Models

        E:\workspace\django\ForumWarga\django-forum-warga (main)
        (venv3932) λ python manage.py makemigrations
        Migrations for 'boards':
          apps\boards\migrations\0001_initial.py
            - Create model Board
            - Create model Topic
            - Create model Post
        
        E:\workspace\django\ForumWarga\django-forum-warga (main)
        (venv3932) λ python manage.py migrate

        modified:   README.md
        new file:   apps/boards/migrations/0001_initial.py

#### 2.8.15 Superuser: Create superuser

        E:\workspace\django\ForumWarga\django-forum-warga (main)
        (venv3932) λ python manage.py createsuperuser

        modified:   README.md

#### 2.9.16 Registering models to admin

        modified:   README.md
        modified:   apps/boards/admin.py

#### 2.10.17 Create some boards entries

        modified:   README.md  

#### 2.11.18 Use Home Views function to render boards data

        modified:   README.md
        modified:   apps/boards/views.py

#### 2.12.19 Create templates and home page

        modified:   README.md
        new file:   apps/boards/templates/home.html
        modified:   apps/boards/views.py

#### 2.13.20 Modified home page by adding table

        modified:   README.md
        modified:   apps/boards/templates/home.html 

#### 2.14.21 Static Files and Bootstrap Setup: modified home page

        modified:   README.md
        modified:   apps/boards/templates/home.html
        ...
        new file:   static/js/simplemde.min.js


### -----------------
### 3. URLS AND FORMS
### -----------------


#### 3.1.22 Adding root URLconf to settings file

        modified:   config/settings.py

#### 3.2.23 Create view function, urls and template for board_topics

        modified:   README.md
        new file:   apps/boards/templates/boards/topics.html
        modified:   apps/boards/views.py
        modified:   config/settings.py
        modified:   config/urls.py

#### 3.3.24 Creating not found page

        modified:   README.md
        modified:   apps/boards/views.py

#### 3.4.25 Page not found - A better way to show it

        modified:   README.md
        modified:   apps/boards/views.py

        NOTE: same result as above

#### 3.5.26 Dynamically showing single board by adding link

        modified:   README.md
        modified:   apps/boards/templates/home.htm

#### 3.6.27 Adding dynamic breadcrumb to topics page

        modified:   README.md
        modified:   apps/boards/templates/boards/topics.html
        modified:   apps/boards/views.py

#### 3.7.28 Django Template Engine Setup: Activate template engine

        modified:   README.md
        modified:   config/settings.py

#### 3.8.29 Django Template Engine Setup: Creating base template to use template inheritance

        modified:   README.md
        new file:   templates/base.html

#### 3.9.30 Django Template Engine Setup: refactor home and topics pages

        modified:   README.md
        new file:   apps/boards/templates/boards/home.html
        modified:   apps/boards/templates/boards/topics.html
        deleted:    apps/boards/templates/home.html
        modified:   apps/boards/views.py 

#### 3.10.31 Adding top bar with a menu

        modified:   README.md
        modified:   templates/base.html

#### 3.11.32 Adding google fonts

        modified:   README.md
        modified:   templates/base.html

#### 3.12.33 FORM - Part 1: Creating a url for new topic 

        modified:   README.md
        modified:   config/urls.py

#### 3.13.34 FORM - Part 2: Creating view function for new topic

        modified:   README.md
        modified:   apps/boards/views.py 

#### 3.14.35 FORM - Part 3: Creating new topic template

        modified:   README.md
        new file:   apps/boards/templates/boards/new_topic.html

#### 3.15.36 FORM - Part 4: Adding form to new topic template

        modified:   README.md
        modified:   apps/boards/templates/boards/new_topic.html

#### 3.16.37 Modified new_topic view function and created a message

        modified:   README.md
        modified:   apps/boards/views.py

#### 3.17.38 LISTING - Rendering topics

        modified:   README.md
        modified:   apps/boards/templates/boards/topics.html

#### 3.18.39 Modified Topic and Post models to show Posts and Topics instances in admin dasboard

        modified:   README.md             
        modified:   apps/boards/models.py 

#### 3.19.40 Adding a button to link the topic and new_topic pages

        modified:   README.md
        modified:   apps/boards/templates/boards/topics.html

#### 3.20.41 DJANGO FORM MODULE - Part 1, Create NewTopicForm model

        modified:   README.md
        new file:   apps/boards/forms.py

#### 3.21.42 DJANGO FORM MODULE - Part 2, Refactoring new_topic view

        modified:   README.md
        modified:   apps/boards/forms.py
        modified:   apps/boards/views.py

#### 3.22.43 DJANGO FORM MODULE - Part 3, Using Django Forms API to Generate HTML

        modified:   README.md
        modified:   apps/boards/templates/boards/new_topic.html  

#### 3.23.44 DJANGO FORM MODULE - Part 4, Adding help text to form

        modified:   README.md
        modified:   apps/boards/forms.py 

#### 3.24.45 Rendering Bootstrap Forms - Part 1, Install django-widget-tweaks

        E:\workspace\django\ForumWarga\django-forum-warga (main)
        (venv3932) λ pip install django-widget-tweaks

        modified:   README.md
        modified:   config/settings.py

#### 3.25.46 Rendering Bootstrap Forms - Part 2, Using Bootstrap widgets

        modified:   README.md
        modified:   apps/boards/templates/boards/new_topic.html

#### 3.26.47 Rendering Bootstrap Forms - Part 3,  Implement the Bootstrap 4 validation tags

        modified:   README.md
        modified:   apps/boards/templates/boards/new_topic.html


#### 3.27.48 Reusable Forms Templates - Includes

        modified:   README.md
        modified:   apps/boards/templates/boards/new_topic.html
        new file:   apps/boards/templates/includes/form.html 


### -------------------------------
### 4. DJANGO AUTHENTICATION SYSTEM
### -------------------------------


#### 4.1.49 Creating a new app 'apps/accounts' and register it to settigns.py

        E:\workspace\django\ForumWarga\django-forum-warga (main)
        (venv3932) λ mkdir apps\accounts

        (venv3932) λ python manage.py startapp accounts apps/accounts

        (venv3932) λ python manage.py check
        System check identified no issues (0 silenced).

#### 4.2.59 Current project structures

        .
        ├── README.md
        ├── apps
        │   ├── accounts
        │   │   ├── __init__.py
        │   │   ├── __pycache__
        │   │   ├── admin.py
        │   │   ├── apps.py
        │   │   ├── migrations
        │   │   ├── models.py
        │   │   ├── tests.py
        │   │   └── views.py
        │   └── boards
        │       ├── __init__.py
        │       ├── __pycache__
        │       ├── admin.py
        │       ├── apps.py
        │       ├── forms.py
        │       ├── migrations
        │       ├── models.py
        │       ├── templates
        │       ├── tests.py
        │       └── views.py
        ├── config
        │   ├── __init__.py
        │   ├── __pycache__
        │   │   ├── __init__.cpython-39.pyc
        │   │   ├── settings.cpython-39.pyc
        │   │   ├── urls.cpython-39.pyc
        │   │   └── wsgi.cpython-39.pyc
        │   ├── asgi.py
        │   ├── settings.py
        │   ├── urls.py
        │   └── wsgi.py
        ├── db.sqlite3
        ├── manage.py
        ├── static
        │   ├── css
        │   │   ├── accounts.css
        │   │   ├── app.css
        │   │   ├── bootstrap.min.css
        │   │   └── simplemde.min.css
        │   ├── img
        │   │   ├── DO_Powered_by_Badge_black.png
        │   │   ├── avatar.svg
        │   │   └── shattered.png
        │   └── js
        │       ├── bootstrap.min.js
        │       ├── jquery-3.2.1.min.js
        │       ├── popper.min.js
        │       └── simplemde.min.js
        ├── templates
        │   └── base.html
        └── venv3932

#### 4.3.60 Creating signup page

        modified:   README.md
        new file:   apps/accounts/templates/accounts/signup.html
        modified:   apps/accounts/views.py
        modified:   config/urls.py 

#### 4.4.61 Hidding (Blocking) navar and breadcrumb for signup, login or user authenticaton pages

        modified:   README.md
        modified:   apps/accounts/templates/accounts/signup.html
        modified:   templates/base.html

#### 4.5.62 Creating signup form

        modified:   README.md
        modified:   apps/accounts/templates/accounts/signup.html
        modified:   apps/accounts/views.py

#### 4.6.63 Using form.html template for signup form

        modified:   README.md
        modified:   apps/accounts/templates/accounts/signup.html

#### 4.7.64 Creating form template for accounts and modified includes in boards app, and adding security to form.html template

        modified:   README.md
        new file:   apps/accounts/templates/accounts/includes/form.html
        modified:   apps/accounts/templates/accounts/signup.html
        renamed:    apps/boards/templates/includes/form.html -> apps/boards/templates/boards/includes/form.html
        modified:   apps/boards/templates/boards/new_topic.html

#### 4.8.65 Bussines loci signup view and the validation

        modified:   README.md
        modified:   apps/accounts/views.py

#### 4.9.66 Referencing (showing) the Authenticated User in the Template 

        modified:   README.md
        modified:   templates/base.html

#### 4.10.67 Adding the Email Field to the Form - Part 1, Create SignUpForm class

        modified:   README.md
        new file:   apps/accounts/forms.py

#### 4.11.68 Adding the Email Field to the Form - Part 2, Using the SignUpForm class

        modified:   README.md
        modified:   apps/accounts/views.py


#### 4.12.69 Adding the Email Field to the Form - Part 3, Improving the Sign Up Template


        modified:   README.md
        modified:   apps/accounts/templates/accounts/signup.html
        modified:   apps/accounts/views.py

#### 4.13.70 Logout

        modified:   README.md
        modified:   config/settings.py
        modified:   config/urls.py

#### 4.14.71 Displaying Menu For Authenticated Users - Part 1, Adding dropdown menu

        modified:   README.md
        modified:   templates/base.html

#### 4.15.72 Displaying Menu For Authenticated Users - Part 2, Adding conditional to navbar menu to show menu to authenticated and not-authenticated user

        modified:   README.md
        modified:   templates/base.html

#### 4.16.73 Login

        new file:   apps/accounts/templates/accounts/login.html
        modified:   apps/accounts/templates/accounts/signup.html
        modified:   config/settings.py
        modified:   config/urls.py
        modified:   templates/base.html

#### 4.17.74 Creating base_accounts template

        modified:   README.md
        new file:   apps/accounts/templates/base_accounts.html

#### 4.18.75 Using the base_account template for the login and signup pages

        modified:   README.md
        modified:   apps/accounts/templates/accounts/login.html
        modified:   apps/accounts/templates/accounts/signup.html 

#### 4.19.76 Adding security message on form

        modified:   README.md
        modified:   apps/accounts/templates/accounts/includes/form.html
        modified:   apps/boards/templates/boards/includes/form.html

#### 4.20.78 Template Tags - Part 1, Creating Custom

        modified:   README.md
        new file:   apps/accounts/templatetags/__init__.py
        new file:   apps/accounts/templatetags/form_tags.py
        new file:   apps/boards/templatetags/__init__.py
        new file:   apps/boards/templatetags/form_tags.py

#### 4.21.79 Template Tags - Part 2, Using the templatetags

        modified:   README.md
        modified:   apps/accounts/templates/accounts/includes/form.html
        modified:   apps/boards/templates/boards/includes/form.html
        modified:   apps/boards/templatetags/form_tags.py


#### 4.22.80 Password Reset - Part 1, Console Email Backend

        modified:   README.md
        modified:   config/settings.py


#### 4.23.81 Password Reset - Part 2, Configuring the Routes

        modified:   README.md
        modified:   config/urls.py

#### 4.24.82 Password Reset - Part 3, Create templates

        modified:   README.md
        new file:   apps/accounts/templates/accounts/registration/password_reset.html
        new file:   apps/accounts/templates/accounts/registration/password_reset_confirm.html
        new file:   apps/accounts/templates/accounts/registration/password_reset_done.html
        new file:   apps/accounts/templates/accounts/registration/password_reset_email.html
        new file:   apps/accounts/templates/accounts/registration/password_reset_subject.txt
        new file:   apps/accounts/templates/accounts/registration/password_reset_template.html

#### 4.25.84 Password Reset - Part 4, Adding templates and test

        modified:   .gitignore
        modified:   README.md
        new file:   apps/accounts/templates/accounts/registration/password_change.html
        new file:   apps/accounts/templates/accounts/registration/password_change_done.html
        new file:   apps/accounts/templates/accounts/registration/password_reset.html
        new file:   apps/accounts/templates/accounts/registration/password_reset_complate.html
        new file:   apps/accounts/templates/accounts/registration/password_reset_confirm.html
        new file:   apps/accounts/templates/accounts/registration/password_reset_done.html
        new file:   apps/accounts/templates/accounts/registration/password_reset_email.html
        new file:   apps/accounts/templates/accounts/registration/password_reset_subject.txt
        new file:   apps/accounts/tests/test_view_password_reset.py
        modified:   config/settings.py
        modified:   config/urls.py
        new file:   templates/registration/login.html
        new file:   templates/registration/loginORI.html
        new file:   templates/registration/password_change_done.html
        new file:   templates/registration/password_change_form.html
        new file:   templates/registration/password_reset.html
        new file:   templates/registration/password_reset_complete.html
        new file:   templates/registration/password_reset_confirm.html
        new file:   templates/registration/password_reset_done.html
        new file:   templates/registration/password_reset_email.html
        new file:   templates/registration/password_reset_subject.txt


### --------------------
### 5. PROTECTING VIEWS
### --------------------


#### 5.1.73 Protecting create topic from un-authenticated user

        modified:   README.md
        modified:   apps/boards/views.py


#### 5.2.74 Configuring Login Next Redirect

        http://127.0.0.1:8000/login/?next=/boards/1/new/

        Notice the query string ?next=/boards/1/new/. We can improve the log in template to make use of the next variable and improve the user experience.

        Then if we try to log in now, the application will direct us back to where we were.

        modified:   README.md
        modified:   apps/accounts/templates/accounts/login.html


#### 5.3.75 Accessing the Authenticated User


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

        modified:   README.md
        modified:   apps/boards/views.py


#### 5.4.76 Topic Posts View - rendering:http://127.0.0.1:8000/boards/1/topics/1/

        # http://127.0.0.1:8000/boards/1/topics/1/

        # Boards /Django / Hallo every one

        modified:   README.md
        new file:   apps/boards/templates/boards/topic_posts.html
        modified:   apps/boards/views.py
        modified:   config/urls.py


#### 5.5.77 Topic Posts - Rendering all Topic Posts

        modified:   README.md
        modified:   apps/boards/templates/boards/topic_posts.html


#### 5.6.78 Adding link to topics to show topic detail

        modified:   README.md
        modified:   apps/boards/templates/boards/topics.html


#### 5.7.79 Reply Post View

        modified:   README.md
        modified:   apps/boards/forms.py
        new file:   apps/boards/templates/boards/reply_topic.html
        modified:   apps/boards/views.py
        modified:   config/urls.py

#### 5.8.80 Changing the starter post, so to give it more emphasis in the page

        modified:   README.md
        modified:   apps/boards/forms.py
        new file:   apps/boards/templates/boards/reply_topic.html
        modified:   apps/boards/templates/boards/topic_posts.html
        modified:   apps/boards/views.py
        modified:   config/urls.py


#### 5.9.81 Modified Board, Topic and Post models

        modified:   README.md
        modified:   apps/boards/models.py

#### 5.10.81 Improving the home page template to show counts of posts, topics and link to show detail post

        modified:   README.md
        modified:   apps/boards/models.py
        modified:   apps/boards/templates/boards/home.html

#### 5.11.82 Improve the topics listing view.

        modified:   README.md
        modified:   apps/boards/templates/boards/topics.html
        modified:   apps/boards/views.py

#### 5.12.83 Adding more field to Topic model and run migration

        modified:   README.md
        new file:   apps/boards/migrations/0002_topic_views.py
        modified:   apps/boards/models.py

#### 5.13.84 Tracking the number of views of a given topic is receiving

        modified:   README.md
        modified:   apps/boards/templates/boards/topic_posts.html
        modified:   apps/boards/templates/boards/topics.html
        modified:   apps/boards/views.py


#### -------------------------------------------------------
#### PART 6: CLASS-BASED VIEWS AND GENERIC CLASS-BASED VIEWS
#### -------------------------------------------------------


#### 6.1.85 Using GCBV - Part 1, Create PostUpdateView

        modified:   README.md
        new file:   apps/boards/templates/boards/edit_post.html
        modified:   apps/boards/templates/boards/topic_posts.html
        modified:   apps/boards/views.py
        modified:   config/urls.py


#### 6.2.86 Using GCBV - Part 2, Adding method_decorator to PostUpdateView

        modified:   README.md
        modified:   apps/boards/views.py


#### 6.3.87 Using GCBV - Part 2, Dealing with the other users editing any posts 

        modified:   README.md
        modified:   apps/boards/views.py


#### 6.4.88 Using GCBV - Using ListView to rendering list of posts in the home page by replecing home view by BoardListView

        modified:   README.md
        modified:   apps/boards/views.py
        modified:   config/urls.py  


#### ----------------------------------------------
#### PART 6: PAGINATION - Working on board_topics
#### ----------------------------------------------


#### 6.1.89 Creating 100 Django posts from the python shell

        E:\workspace\django\ForumWarga\django-forum-warga (main)
        (venv3932) λ python manage.py shell
        ...
        >>> from django.contrib.auth.models import User
        >>> from boards.models import Board, Topic, Post
        >>> from apps.boards.models import Board, Topic, Post
        >>> user = User.objects.first()
        >>> board = Board.objects.get(name='Django')
        >>> for i in range(100):
        ...     subject = 'Topic test #{}'.format(i)
        ...     topic = Topic.objects.create(subject=subject, board=board, starter=user)
        ...     Post.objects.create(message='Lorem ipsum...', topic=topic, created_by=user)
        ...
        <Post: Lorem ipsum...>
        <Post: Lorem ipsum...>
        ...
        <Post: Lorem ipsum...>        

        modified:   README.md


#### 6.2.90 Making pagination with FBV Pagination (no magic) - Modified board_topics view

        modified:   README.md
        modified:   apps/boards/views.py


#### 6.2.90 Making pagination with FBV Pagination (no magic) - Adding pagination to boards/topic.html page

        modified:   README.md
        modified:   apps/boards/templates/boards/topics.html
        modified:   apps/boards/views.py


#### -------------------------------------------
#### PART 6: PAGINATION - Working on ListView
#### -------------------------------------------

#### 6.3.91 Making pagination using GCBV (with magic) - Changing board_topics view with TopicListView 

        modified:   README.md
        modified:   apps/boards/templates/boards/topics.html
        modified:   apps/boards/views.py
        modified:   config/urls.py


#### 6.4.92 Making pagination using GCBV (with magic) - Paginate the topic posts page (Reusable Pagination Template)

        modified:   README.md
        new file:   apps/boards/templates/boards/includes/pagination.html
        modified:   apps/boards/templates/boards/topic_posts.html
        modified:   apps/boards/templates/boards/topics.html
        modified:   apps/boards/views.py
        modified:   config/urls.py


#### -------------------------
#### PART 6: MY ACCOUNT VIEW 
#### -------------------------


#### 6.1.93 Creating my_account page and UserUpdateView

        modified:   README.md
        new file:   apps/accounts/templates/accounts/my_account.html
        modified:   apps/accounts/views.py
        modified:   apps/boards/views.py
        modified:   config/urls.py


#### 6.2.94 Markdown - Install markdown and use it Post model

        E:\workspace\django\ForumWarga\django-forum-warga (main)
        (venv3932) λ pip install markdown

        modified:   README.md
        modified:   apps/boards/models.py
        modified:   apps/boards/templates/boards/reply_topic.html
        modified:   apps/boards/templates/boards/topic_posts.html


#### 6.3.95 Markdown Editor - Adding Markdown Editor to topic_posts and reply_topic pages

        modified:   README.md
        modified:   apps/boards/templates/boards/edit_post.html
        modified:   apps/boards/templates/boards/reply_topic.html
        modified:   templates/base.html 


#### ------------------
#### PART 6: HUMANIZE 
#### ------------------

#### 6.1.96 Adding humanize to topic page

        modified:   README.md
        modified:   apps/boards/templates/boards/topics.html
        modified:   config/settings.py


#### ------------------
#### PART 6: GRAVATAR 
#### ------------------


#### 6.1.98 Adding gravatar to topic_posts page

        modified:   README.md
        modified:   apps/boards/templates/boards/topic_posts.html
        new file:   apps/boards/templatetags/gravatar.py



#### ---------------------------
#### PART 6: FINAL ADJUSTMENT
#### ---------------------------


#### 6.1.99 Updating last_update post replies

        modified:   README.md
        modified:   apps/boards/views.py


#### 6.2.100 Controlling the view counting system

        modified:   README.md
        modified:   apps/boards/views.py

#### 6.3.101 provide a better navigation in the topics listing        
        """
        Currently the only option is for the user to click in the topic title and go to the first page. We could workout something like this:
        """

        modified:   README.md
        modified:   apps/boards/models.py


#### 6.4.102 Adjusting the number of pages to show the pagination in  topi list


        modified:   apps/boards/models.py
        modified:   apps/boards/templates/boards/topics.html
        modified:   apps/boards/views.py

#### 6.5.105 Limitting replies showed in reply page

        """
        In the reply page, we are currently listing all topic replies. We could limit it to just the last ten posts.
        """         

        modified:   README.md
        modified:   apps/boards/models.py
        modified:   apps/boards/templates/boards/reply_topic.html


#### 6.6.106 Redirecting user to last page after posting a reply

        """
        Another thing is that when the user replies to a post, we are redirecting the user to the first page again. We could improve it by sending the user to the last page.
        """

        modified:   README.md
        modified:   apps/boards/templates/boards/topic_posts.html
        modified:   apps/boards/views.py