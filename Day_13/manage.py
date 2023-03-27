#!/usr/bin/env python
"""In a Django project, manage.py is a command-line utility that provides a number of useful functions for managing the project, including:

    Running the development server: manage.py runserver starts the Django development server, which allows you to view your application in a web browser and test your code changes locally.

    Creating a new Django application: manage.py startapp appname creates a new Django application with the specified name. This command generates a directory structure and several files that are needed to get started with the new application.

    Creating database tables: manage.py migrate applies any pending database migrations to create or update database tables based on changes in your models.

    Creating a new superuser: manage.py createsuperuser creates a new superuser account that can be used to access the Django admin interface.

    Running tests: manage.py test runs automated tests for the project and its applications.

    Checking for errors: manage.py check checks the project for common errors, such as missing migrations, syntax errors, or configuration problems.

Overall, manage.py is a powerful tool that allows you to interact with your Django project from the command line, perform common development tasks, and automate common workflows."""

"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
