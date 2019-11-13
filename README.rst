=====
Django Reusable Core
=====

Django Reusable Core é uma aplicação base ser usada em varios microserviços. O mesmo conta com funcionalidades genericas.

Quick start
-----------

1. Add "django-reusable-core" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        ...
        'reusable_core',
    ]

2. Include the middleware in middleware settings.py like this::

    MIDDLEWARE = [
        ...
        'django.contrib.auth.middleware.AuthenticationMiddleware',        
        'apps.reusable_core.middleware.ReusableClientMiddleware',
        ...
    ]

3. Run `python manage.py migrate` to create the django-reusable-core models.

4. enjoy it!
