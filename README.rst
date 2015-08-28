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

1. Add "menu", flatpages and sites to your INSTALLED_APPS setting like this::

      INSTALLED_APPS = (
          ...
	  'django.contrib.flatpages',
    	  'django.contrib.sites',
          'menu',
      )

2. Run `python manage.py syncdb` to create the menu models.

3. Start the development server and visit http://127.0.0.1:8000/admin/
   to create a menu (you'll need the Admin app enabled).

4. You can use it in your context processors or views.

Requirements
------------
django==1.6.5, feincms
