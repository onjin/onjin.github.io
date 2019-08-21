---
title: "porządki na dysku, czyli mv, ln, mount i bind"
date: 2009-05-12T22:46:59
slug: blog20090512porzadki-na-dysku-czyli-mv-ln-mount-i-bind
tags: ["linux"]
---
<html><body><p>Robiąc ostatnio trochę miejsca pomiędzy partycjami przeniosłem <em>/usr/lib</em> do <em>/opt/usr/lib</em> i zrobiłem symlink <em>ln -s /opt/usr/lib /usr/lib</em>. Problemem okazało się np <em>/usr/lib/cups/filter/foomatic-rip</em>, który jest linkiem  relatywnym do <em>../../../bin/foomatic-rip</em> i w ten sposób pozbyłem się możliwości drukowania.


Nie mam miejsca by zrobić/użyć partycji, którą bym zamontował pod <em>/usr/lib</em> ale chwila w necie pozoliła znaleść mi rozwiązanie odpowiednie dla mnie :)



</p><blockquote>

mount --bind /opt/usr/lib /usr/lib

</blockquote>



lub w <strong>/etc/fstab</strong>

<blockquote>

/opt/usr/lib /usr/lib none bind

</blockquote>



i teraz jest ok :)</body></html>