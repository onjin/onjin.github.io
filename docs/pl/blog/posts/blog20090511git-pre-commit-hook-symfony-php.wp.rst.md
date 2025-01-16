---
title: "git pre-commit hook - symfony / php"
date: 2009-05-11T10:25:43
tags: ["git","php","python","tools"]
---
Mam jeszcze tą nieprzyjemnośc pracy z PHP (w tym przypadku z symfony framework) i aby była przyjemniejsza dodałem sobie hook na **pre-commit** do git'a.
 * <a href="http://dl.getdropbox.com/u/185133/git/pre-commit">http://dl.getdropbox.com/u/185133/git/pre-commit</a>

by zadziałało przerywanie commit'a gdy '*symfony unit-test*' się nie udadzą, potrzebna jest łatka na symfony (przynajmniej na moją wersję 1.0.17)
 * <a href="http://dl.getdropbox.com/u/185133/git/symfony_return_code.diff">http://dl.getdropbox.com/u/185133/git/symfony_return_code.diff</a>

Hook zakłada, że commit jest robiony w katalogu projektu (tak mam najczęsciej) i znajduje sie w nim plik 'symfony'

btw: hook wymaga pythona.
