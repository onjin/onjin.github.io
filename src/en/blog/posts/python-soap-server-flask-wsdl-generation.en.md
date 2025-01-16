---
title: "Python SOAP server (flask) + wsdl generation"
date: 2013-08-13T18:53:49
url: /posts/blog20130813python-soap-server-flask-wsdl-generation.html
tags: ["programming","python","webdev","flask"]
---

Simple tutorial how quickly create SOAP server using python "Flask-Enterprise" package for "flash" web framework.
Example comes with basic client using "suds" package.


<!-- more -->

## Install

```bash

$ pip install Flask-Enterprise

```

## Create app file


```python linenums="1" title="soap.py"

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



## Run service

```bash

$ python soap.py

```


## Create client

```python linenums="1" title="client.py"

from suds.client import Client

c = Client('http://127.0.0.1:5555/soap?wsdl')
print c.service.get_time()

```


## Run test

```bash

$ python client.py
Tue Aug 13 19:49:53 2013
```
