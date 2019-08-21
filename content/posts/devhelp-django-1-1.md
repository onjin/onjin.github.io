---
title: "devhelp + django 1.1"
date: 2010-04-26T19:51:34+01:00
slug: blog20100426devhelp-django-1-1
tags: ["devhelp", "django", "python" ]
---

Ostatnio biegałem z lapkiem po centrum handlowym i łapałem wifi, żeby spojrzeć do dokumentacji <a href="http://www.djangoproject.com/">django</a>. I tylko się nabiegałem :).


Aby drugi raz pracować nie biegać w domu szybko podłączyłem dokumentację django do <a href="http://live.gnome.org/devhelp">devhelp</a> i tak na szybko procedura:

{{< highlight bash >}}
apt-get install devhelp

mkdir -p ~/bin; cd ~/bin
wget http://htmlhelp.googlecode.com/svn/trunk/misc/devhelp-install
chmod +x devhelp-install

cd ~/; wget http://onjin.net/files/django1.1-doc.tgz 
/bin/devhelp-install ./django1.1-doc.tgz
{{< /highlight >}}



Teraz wystarczy uruchomić devhelp'a i cieszyć się offline :)


django1.1-doc jest ściągnięte z <a href="http://charupload.wordpress.com/2007/12/02/django-documentation-chm/">.chm</a> i potraktowana <a href="http://code.google.com/p/htmlhelp/source/browse/trunk/pyhtmlhelp/hhconvert.py">hhconvert.py</a> do formatu devhelp'a)
