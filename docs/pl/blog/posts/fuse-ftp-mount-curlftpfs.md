---
title: "fuse ftp mount - curlftpfs"
date: 2009-06-21T19:11:10
tags: ["ftp","ftpmount","linux","python"]
---
<div style="text-align: center; border-bottom: solid 1px gray; background: orange">sprawdź najnowszą wersję <a href="https://github.com/onjin/ftpmount">ftpmount</a></div>

---

Do pracy z hostingiem gdzie mamy tylko '''ftp''' przydaje się montowanie dysku poprzez właśnie ftp. Służy do tego program '''curlftpfs''' (np apt-get install curlftpfs).


Odpalamy go jako:

```bash
$ curlftpfs ftp://user:pass@host/ ./mountpoint
```


Do tego potrzebujemy uprawnienia grupy `fuse` więć jako `root` musimy sobie ją dodać od naszego użytkownika.

Jeżeli mamy dużo połączeń do zarządzania przyda się mały skrypt:

* <a href="http://onjin.net/files/ftpmount">ftpmount</a>


sterowany konfiguracją w pliku `config.ini`:

```dosini
[hostone.pl]
host=ftp.hostone.pl
user=userone
pass=passone # jak nie podamy tego wpisu, program się zapyta o hasło
mountpoint=hostone.pl

[hosttwo.pl]
host=ftp.hosttwo.pl
user=usertwo
mountpoint=hosttwo.pl
```

Wtedy wystarczy nam:

 * ./ftpmount hostone.pl   # montujemy połączenie
 * ./ftpmount -u hostone.pl   #odmontowywujemy połączenie
 * ./ftpmount -l   # lista dostępnych konfiguracji połączeń
