---
title: "home.pl & django - pierwsza potyczka"
date: 2009-02-26T21:59:38+01:00
url: /posts/blog20090226homepl-django-pierwsza-potyczka.html
tags: ["hosting", "webdev", "django", "home.pl", "python"]
toc: true
---

*home.pl* obsługuje **pythona** jako **cgi** (pliki .py) więc tego będziemy się trzymać. Instalację wykonamy w katalogu **/py**


## Instalacja django

hardcoded ale działa ;) wrzucamy to do /py i ruchamiamy poprzez www (plik install.py)

```python linenums="1" title="install.py"
    #!/usr/bin/env python

    import os

    os.system("wget http://www.djangoproject.com/download/1.0.2/tarball/")
    os.system("tar zxf Django-1.0.2-final.tar.gz")
    os.system("rm Django-1.0.2-final.tar.gz")
    os.system("mv Django-1.0.2-final tmp")
    os.system("mv tmp/django django")
```

## nasz projekt

Lokalnie wołamy

```bash
    $ django-admin.py startproject pytest
```

i wrzucamy katalog *pytest* przez ftp na home do katalogu /py .



```python linenums="1" title="dispatch.py"
#!/usr/bin/env python

import os, sys
import django.core.handlers.wsgi

def run_with_cgi(application):

    environ                      = dict(os.environ.items())
    environ['wsgi.input']        = sys.stdin
    environ['wsgi.errors']       = sys.stderr
    environ['wsgi.version']      = (1,0)
    environ['wsgi.multithread']  = False
    environ['wsgi.multiprocess'] = True
    environ['wsgi.run_once']     = True

    if environ.get('HTTPS','off') in ('on','1'):
        environ['wsgi.url_scheme'] = 'https'
    else:
        environ['wsgi.url_scheme'] = 'http'

    headers_set  = []
    headers_sent = []

    def write(data):
        if not headers_set:
            raise AssertionError("write() before start_response()")

        elif not headers_sent:
            # Before the first output, send the stored headers
            status, response_headers = headers_sent[:] = headers_set
            sys.stdout.write('Status: %s\\r\\n' % status)
            for header in response_headers:
                sys.stdout.write('%s: %s\\r\\n' % header)
            sys.stdout.write('\\r\\n')

        sys.stdout.write(data)
        sys.stdout.flush()

    def start_response(status,response_headers,exc_info=None):
        if exc_info:
            try:
                if headers_sent:
                    # Re-raise original exception if headers sent
                    raise exc_info[0], exc_info[1], exc_info[2]
            finally:
                exc_info = None     # avoid dangling circular ref
        elif headers_set:
            raise AssertionError("Headers already set!")

        headers_set[:] = [status,response_headers]
        return write

    result = application(environ, start_response)
    try:
        for data in result:
            if data:    # don't send headers until body appears
                write(data)
        if not headers_sent:
            write('')   # send headers now if body was empty
    finally:
        if hasattr(result,'close'):
        result.close()


# Change this to the directory above your site code.
sys.path.append("/py")

# Change mysite to the name of your site package
os.environ['DJANGO_SETTINGS_MODULE'] = 'pytest.settings'

run_with_cgi(django.core.handlers.wsgi.WSGIHandler())
```


i odpalamy to by www :D na razie tyle ...


## do pobrania

Dokładam paczkę z plikami do testu:

 * [pyzip]

```bash
    $ unzip py.zip
```


ftp na home.pl; open http://server.home.pl/py/dispatch.py/admin


## dodatkowe moje narzędzia

 * [django-buildout-template] - szablon startowy dla projektów django z monitoringiem procesów, itp.
 * [vim-startup] - vim dostosowany do edycji python'a


[django-buildout-template]: https://github.com/onjin/django-buildout-template
[vim-startup]: https://github.com/onjin/vim-startup
[pyzip]: https://dl.dropboxusercontent.com/u/185133/marekwywial.name/files/py.zip
