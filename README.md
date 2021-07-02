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

#### 2.6.14 Migrating the Models

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


























































































































































































































