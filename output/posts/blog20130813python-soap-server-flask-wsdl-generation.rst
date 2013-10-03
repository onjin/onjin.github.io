.. title: Python SOAP server (flask) + wsdl generation
.. slug: blog20130813python-soap-server-flask-wsdl-generation
.. date: 2013-08-13 18:53:49
.. tags: onjin,programowanie,python,webdev


Install
-------
.. code:: bash

    $ pip install Flask-Enterprise



file: soap.py
-------------

.. code:: python
    :number-lines:

    from time import ctime
    from flask import Flask
    from flaskext.enterprise import Enterprise

    app = Flask(__name__)

    enterprise = Enterprise(app)


    class DemoService(enterprise.SOAPService):
        __soap_server_address__ = '/soap'
        __soap_target_namespace__ = 'ns'

        @enterprise.soap(_returns=enterprise._sp.String)
        def get_time(self):
            return ctime()

    if __name__ == '__main__':
        app.run(host='127.0.0.1', port=5555)



Run service
-----------

.. code:: bash

    $ python soap.py


file: client.py
---------------

.. code:: python
    :number-lines:

    from suds.client import Client

    c = Client('http://127.0.0.1:5555/soap?wsdl')
    print c.service.get_time()


Run test
--------

.. code:: bash

    $ python client.py
    Tue Aug 13 19:49:53 2013
