WANRNING
===========================
This fork is still in the early stages of development and usage is discouraged.
At least for now. We'll let you know when the cookies are ready :)


PyBBM Django forum solution + Sub-Boards
===========================
PyBBM - modified version of pybb (developed by lorien and dropped in mid 2010).

`Documentation aviable on ReadTheDocs <http://readthedocs.org/projects/pybbm/>`_

PyBBM includes ready to use `example/test project with instructions <http://readthedocs.org/docs/pybbm/en/latest/example.html>`_

The main point in development of pybb is to build it so it could be
*easily* integrated to existing django based site. This mean:

* pybb does not provide features like user registration, password restoring.
  It does not provide authentication page. You should use your favorite
  application for such things. You can try well known django-registration
  http://code.google.com/p/django-registration/.

i18n support
============
PYBB support only english and russian translations now.
You should enable django.middleware.locale.LocaleMiddleware to activate
django locale autodetecting.

What is the purpose of this fork?
============
I need to add sub-boards as well as some other features to pybbm.

TO-DO List
============
* Picture for Forums
* Mptt https://github.com/django-mptt/django-mptt/
