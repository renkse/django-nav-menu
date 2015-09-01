=====
django-nav-menu
=====

django-nav-menu is a Django app for creating the simplest menu trees in admin panel.

=====
WARNING!!!
=====
This app works only with django 1.6.5

Quick start
-----------

1. You can install django-nav-menu through pip:
      pip install django-nav-menu
   or check out last version from github: https://github.com/renkse/django-nav-menu.git

2. Add "menu", flatpages and sites to your INSTALLED_APPS setting like this::

      INSTALLED_APPS = (
          ...
          'django.contrib.flatpages',
    	  'django.contrib.sites',
          'menu',
      )

3. Run `python manage.py syncdb` to create the menu models.

4. Start the development server and visit http://127.0.0.1:8000/admin/
   to create a menu (you'll need the Admin app enabled).

5. You can use it in your context processors or views.

Requirements
------------
django==1.6.5, feincms
