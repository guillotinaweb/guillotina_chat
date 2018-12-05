guillotina_chat Docs
====================

This is a simple package that is designed to be used as reference material
for the `Guillotina training section of the docs
<http://guillotina.readthedocs.io/en/latest/training/index.html>`_.

It's really not meant for anything other than training so don't expect this
to be useful!


Dependencies
------------

Python >= 3.6


Installation
------------

This example will use virtualenv::

  python -m venv .
  ./bin/pip install -e .[test]


Running
-------

Run pg:

  make run-postgres

Most simple way to get running::

  ./bin/guillotina
