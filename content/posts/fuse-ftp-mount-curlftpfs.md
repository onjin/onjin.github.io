---
title: "fuse ftp mount - curlftpfs"
date: 2009-06-21T19:11:10
slug: blog20090621fuse-ftp-mount-curlftpfs
tags: ["ftp","ftpmount","linux","python"]
cover: /img/cover-network1.jpg
---
<div style="text-align: center; border-bottom: solid 1px gray; background: orange">sprawdź najnowszą wersję <a href="https://github.com/onjin/ftpmount">ftpmount</a></div>

---

Do pracy z hostingiem gdzie mamy tylko '''ftp''' przydaje się montowanie dysku poprzez właśnie ftp. Służy do tego program '''curlftpfs''' (np apt-get install curlftpfs).


Odpalamy go jako:

{{< highlight shell >}}
  $ curlftpfs ftp://user:pass@host/ ./mountpoint
{{< /highlight >}}


Do tego potrzebujemy uprawnienia grupy `fuse` więć jako `root` musimy sobie ją dodać od naszego użytkownika.

Jeżeli mamy dużo połączeń do zarządzania przyda się mały skrypt:

* <a href="http://onjin.net/files/ftpmount">ftpmount</a>


sterowany konfiguracją w pliku `config.ini`:

{{< highlight ini >}}
  [hostone.pl]
  host=ftp.hostone.pl
  user=userone
  pass=passone # jak nie podamy tego wpisu, program się zapyta o hasło
  mountpoint=hostone.pl

  [hosttwo.pl]
  host=ftp.hosttwo.pl
  user=usertwo
  mountpoint=hosttwo.pl
{{< /highlight >}}

Wtedy wystarczy nam:

 * ./ftpmount hostone.pl   # montujemy połączenie
 * ./ftpmount -u hostone.pl   #odmontowywujemy połączenie
 * ./ftpmount -l   # lista dostępnych konfiguracji połączeń
