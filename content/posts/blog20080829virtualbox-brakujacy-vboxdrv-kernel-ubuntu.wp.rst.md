---
title: "virtualbox brakujący vboxdrv kernel + ubuntu"
date: 2008-08-29T08:26:16
slug: blog20080829virtualbox-brakujacy-vboxdrv-kernel-ubuntu
tags: ["linux","tools","ubuntu"]
---
<html><body><p>Czasem w <a href="http://www.ubuntu.pl/">Ubuntu</a> (np przy pakietach proposal) przychodzi wyższa wersja kernela bez upgrade drivera do <a href="http://www.virtualbox.org/">virtualbox'a</a></p>
<p>Wtedy pomaga mi taka kombinacja</p>

<pre>

sudo apt-get install virtualbox-ose-source

sudo m-a update

sudo m-a prepare

sudo m-a a-i virtualbox-ose

sudo /etc/init.d/vboxdrv restart

</pre>

<p>Restart <a href="http://www.virtualbox.org/">virtualbox'a</a> i gotow. Back to work.</p></body></html>