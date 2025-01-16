---
title: "git php syntax check pre-commit"
date: 2010-05-04T07:52:53
tags: ["git", "python","php"]
---
Załączam używany przeze mnie i sprawdzający się <strong>pre-commit</strong> dla <strong>git</strong>'a sprawdzający commitowane pliki .php.

Przy wykonaniu commit w repozytorium skrypt dla każdego commitowanego pliku '<strong>.php</strong>' wykonuje '<strong>php -l</strong>' w pętli, aż otrzyma odpowiedź, że składnia jest ok lub nie ok. Przypadku wystąpienia błędy przerywa commit. Sam skrypt napisany jest w <em>python</em>'ie

Dlaczego w pętli? Dlatego, że 'php -l' losowo się urywa zwracając <em>SIGFAULT</em> i należy wtedy powtórzyć próbę z '-l'


Plik do pobrania:

* <a href="/files/php-l/pre-commit">pre-commit</a>
