================
django-mysqlping
================

|build-status| |pypi| |docs|

Ping to MySQL in Django middleware.

This middleware ping to MySQL server before the request and auto reconnect to the server.

It supports PyMySQL(using MySQLdb mode) and mysqlclient in the database backend of Django(django.db.backends.mysql).

License
=======

This software is licensed under the MIT License.

Author
======

* Shinya Okano

.. |build-status| image:: https://travis-ci.org/tokibito/django-mysqlping.svg?branch=master
   :target: https://travis-ci.org/tokibito/django-mysqlping
.. |docs| image:: https://readthedocs.org/projects/django-mysqlping/badge/?version=latest
   :target: https://readthedocs.org/projects/django-mysqlping/
.. |pypi| image:: https://badge.fury.io/py/django-mysqlping.svg
   :target: http://badge.fury.io/py/django-mysqlping
