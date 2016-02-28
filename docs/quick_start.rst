Quick Start
===========

Install package via ``pip``
::

    pip install django-gddkia-impediments-on-roads

Configure cache options
::

   # Cache backend name
   IMPEDIMENTS_CACHE_BACKEND_NAME = 'default'

   # Cache key
   IMPEDIMENTS_CACHE_KEY = 'impediments'

   # Max time of cache
   IMPEDIMENTS_CACHE_TIMEOUT = 3600

Simple usage
::

    from dj_impediments import get_impediments

    impediments = get_impediments()
