==================================
django-gddkia-impediments-on-roads
==================================

.. image:: https://codeclimate.com/github/tomi77/django-gddkia-impediments-on-roads/badges/gpa.svg
   :target: https://codeclimate.com/github/tomi77/django-gddkia-impediments-on-roads
   :alt: Code Climate

Installation
============

Install package via ``pip``
::

    pip install django-gddkia-impediments-on-roads

Configuration
=============

Configure cache options
::

   # Cache backend name
   IMPEDIMENTS_CACHE_BACKEND_NAME = 'default'

   # Cache key
   IMPEDIMENTS_CACHE_KEY = 'impediments'

   # Max time of cache
   IMPEDIMENTS_CACHE_TIMEOUT = 3600

API Usage
=========

::

    from dj_impediments import get_impediments

    print get_impediments()
