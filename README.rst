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


Setup
-----

To setup the app then, first create container::

    curl -X POST http://localhost:8080/db -d '{"id": "container", "@type": "Container"}' --user root:root

Then, install the app::

    curl -X POST http://localhost:8080/db/container/@addons -d '{"id": "dbusers"}' --user root:root
    curl -X POST http://localhost:8080/db/container/@addons -d '{"id": "guillotina_chat"}' --user root:root


Test, it's working::

    curl http://localhost:8080/db/container/@get-conversations --user root:root


And, test sending message::

    curl -i -X POST http://localhost:8080/db/container/conversations/ --data-raw '{
        "@type": "Conversation",
        "title": "New convo with foobar2", "users": ["Bob", "Alice"] }
    ' --user root:root
