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









































































































































































