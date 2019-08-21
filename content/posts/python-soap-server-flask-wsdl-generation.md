---
title: "Python SOAP server (flask) + wsdl generation"
date: 2013-08-13T18:53:49
slug: blog20130813python-soap-server-flask-wsdl-generation
url: /posts/blog20130813python-soap-server-flask-wsdl-generation.html
tags: ["programowanie","python","webdev","flask"]
cover: /img/cover-flask-wsdl.png
aliases:
    - /posts/blog20130813python-soap-server-flask-wsdl-generation/index.html
---


Install
-------
{{< highlight bash >}}

    $ pip install Flask-Enterprise

{{< /highlight >}}



file: soap.py
-------------


{{< highlight python "linenos=table" >}}
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
{{< /highlight >}}



Run service
-----------

{{< highlight bash >}}

    $ python soap.py

{{< /highlight >}}


file: client.py
---------------

{{< highlight python "linenos=table" >}}

    from suds.client import Client

    c = Client('http://127.0.0.1:5555/soap?wsdl')
    print c.service.get_time()

{{< /highlight >}}


Run test
--------

{{< highlight bash >}}

    $ python client.py
    Tue Aug 13 19:49:53 2013
{{< /highlight >}}
