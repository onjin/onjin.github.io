---
title: "lint dla php"
date: 2008-09-02T21:01:02
slug: blog20080902lint-dla-php
tags: ["php","programowanie","tools","webdev"]
---
<html><body><p>Za dnia piszę najczęściej w <a href="http://php.net">php</a> i zazdroszczę <a href="http://python.org/">pythonowi</a> <a href="http://www.logilab.org/857">pylinta</a>.<br>
Z ciekawości zagooglałem i znalazłem rozwiązanie dla PHP sprawdzające Coding Standard:</p>

<pre>

pear install PHP_CodeSniffer

phpcs --standard=Zend SomeTest.class.php

</pre>

<p><em>phpcs -i</em> podaje dostępne standardy:</p>

<ul><li>PEAR</li>

<li>MySource</li>

<li>PHPCS</li>

<li>Squiz</li>

<li>Zend</li>

</ul><p>Mi najbardzie odpowiada Zend co widać po wynikach lintowania, najczęściej 0 ostrzeżeń i błędów ;).</p>

<p>phpcs pozwala także tworzyć swoje <a href="http://pear.php.net/manual/en/package.php.php-codesniffer.coding-standard-tutorial.php">własne standardy kodowanie</a> oraz - co bardzo mnie cieszy - podpiąć go jako <a href="http://pear.php.net/manual/en/package.php.php-codesniffer.svn-pre-commit.php">precommit hook</a> do <a href="http://subversion.tigris.org/">svn'a</a>.</p></body></html>