---
title: "Grooveshark currentSong.txt + gajim status"
date: 2011-03-19T13:03:04
slug: blog20110319grooveshark-currentsong-txt-gajim-status
url: /posts/blog20110319grooveshark-currentsong-txt-gajim-status.html
tags: ["desktop","linux","music","python","tools"]
cover: /img/cover-music1.jpg
---
Przy okazji szukania API do <a href="http://grooveshark.com">grooveshark'a</a> odkryłem plik <b>currentSong.txt</b>, który jest tworzony przez <em>Grooveshark Desktop</em>.

Kilka minut z vim'em i mamy skrypt napisany w python'ie, który odczytuje w/w plik i wrzuca informację o aktualnie odtwarzanym utworze jako status wybranego konta w <a href="http://gajim.org">gajim'a</a>.

Skrypt umożliwia także uruchomienie go w trybie monitorowania w/w pliku (wymana <b>pyinotify</b>). Wtedy nasz status będzie zmieniany w chwili (chwilę potem :) ) zmiany utworu w Grooveshark Desktop.

Całość można dowolnie używać/modyfikować, a pobrać można z serwisu <a href="http://github.com">github.com</a>:

* <a href="https://github.com/onjin/grooveshark2gajim">https://github.com/onjin/grooveshark2gajim</a>
* <a href="http://onjin.github.com/grooveshark2gajim/">http://onjin.github.com/grooveshark2gajim/</a>


Do działania wystarczy nam plik <a href="https://github.com/onjin/grooveshark2gajim/raw/master/grov2gajim.py">grov2gajim.py</a>. Umieszczamy go gdzieś na dysku i możemy używać.
