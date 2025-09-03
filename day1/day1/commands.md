pip install django

<!-- for django installation -->

django-admin startproject projectname

<!-- for creating the projct  -->

myproject/
│ manage.py
│
└───myproject/
│ **init**.py
│ settings.py
│ urls.py
│ asgi.py
│ wsgi.py

<!-- What each file does:

manage.py → Command-line tool (run server, create apps, run migrations, etc).

settings.py → Main configuration (database, installed apps, templates, static files).

urls.py → All URL routes for the project.

wsgi.py/asgi.py → For deployment (don’t worry too much on Day 1).

__init__.py → Marks folder as a Python package. -->

<!-- Run the Development Server -->

python manage.py runserver

<!-- to create the app -->

python manage.py startapp appname

<!-- example -->

python manage.py startapp blog

blog/
│ admin.py
│ apps.py
│ models.py
│ tests.py
│ views.py
│ urls.py (you create this manually)
│ **init**.py
│ migrations/

<!-- What each file does:

models.py → Database tables (ORM).

views.py → Logic to handle requests (what user sees/gets).

admin.py → Django admin site configuration.

apps.py → Metadata about the app.

tests.py → Unit tests.

migrations/ → Auto-generated files for DB schema changes. -->

Register the App

INSTALLED_APPS = [
...
'blog',
]

python manage.py makemigrations
python manage.py migrate

<!-- 👉 makemigrations → generates instructions.
     👉 migrate → applies changes to the database (SQLite by default)
-->

<!-- Create Superuser (Admin Login) -->

python manage.py createsuperuser

<!-- 👉 This makes Post appear in Django admin dashboard. -->

from django.contrib import admin
from .models import Post

admin.site.register(Post)
