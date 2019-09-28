---
title: "Python SOAP server (flask) + generowanie wsdl"
date: 2013-08-13T18:53:49
slug: blog20130813python-soap-server-flask-wsdl-generation-pl
url: /posts/blog20130813python-soap-server-flask-wsdl-generation-pl.html
tags: ["programming","python","webdev","flask"]
cover: /img/cover-flask-wsdl.png
aliases:
    - /posts/blog20130813python-soap-server-flask-wsdl-generation-pl/index.html
toc: true
---

Krótkie wprowadzenie jak uruchomić prosty serwer SOAP przy pomocy pakietu "Flask-Enterprise".
Do przetestowania połączenia do serwera użyjemy klienta z pakietu "suds".


<!--more-->

# Instalacja
{{< highlight bash >}}

    $ pip install Flask-Enterprise

{{< /highlight >}}



# plik: soap.py


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



## Uruchamiamy serwer

{{< highlight bash >}}

    $ python soap.py

{{< /highlight >}}


# plik: client.py

{{< highlight python "linenos=table" >}}

    from suds.client import Client

    c = Client('http://127.0.0.1:5555/soap?wsdl')
    print c.service.get_time()

{{< /highlight >}}


## Uruchamiamy klienta

{{< highlight bash >}}

    $ python client.py
    Tue Aug 13 19:49:53 2013
{{< /highlight >}}
