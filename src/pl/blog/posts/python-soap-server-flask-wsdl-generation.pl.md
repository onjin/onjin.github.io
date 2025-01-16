---
title: "Python SOAP server (flask) + generowanie wsdl"
date: 2013-08-13T18:53:49
tags: ["programming","python","webdev","flask"]
language: pl
links:
    - url: /en/blog/python-soap-server-flask--wsdl-generation/
      title: Przeczytaj po angielsku
      section: Alternatywy
---

Krótkie wprowadzenie jak uruchomić prosty serwer SOAP przy pomocy pakietu "Flask-Enterprise".
Do przetestowania połączenia do serwera użyjemy klienta z pakietu "suds".


<!-- more -->

## Instalacja

```bash

$ pip install Flask-Enterprise

```


## Tworzenie pliku servera

``` python linenums="1" title="soap.py"

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
```



## Uruchamiamy serwer

```bash

$ python soap.py

```

## Tworzenie pliku klienta

```python linenums="1" title="client.py"

from suds.client import Client

c = Client('http://127.0.0.1:5555/soap?wsdl')
print c.service.get_time()

```


## Uruchamiamy klienta

```bash

$ python client.py
Tue Aug 13 19:49:53 2013
```
