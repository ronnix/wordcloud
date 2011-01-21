
Installation and Setup
======================

Make a Python virtual environment::

    virtualenv --no-site-packages .
    source bin/activate

Install dependencies in the virtualenv::

    pip install -r requirements.txt

Start the server::

    paster serve development.ini

