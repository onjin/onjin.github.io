---
title: "Sortowanie tabel"
date: 2006-01-10T10:04:48
slug: blog20060110sortowanie-tabel
tags: ["www"]
---
Chyba każdy wyrzucił kiedyś na ekran tabelkę w HTML'u. Jeśli danych dużo i dynamiczne, to użył do tego PHP. Aby lepiej ogarnąć dane, nagłówki kolumn zostały odnośnikami z końcówką mniej więcej taką:


{{< highlight html >}}
  <ht><a href="?order=data">data</a>
  <th><a href="?order=ilosc">ilość</a></th>
{{< /highlight >}}

Ta sama tabelka, te same dane. Ale aby ją posortować trzeba znów odwoływać się do serwera. Wygodniej by było gdyby tabelka mogła się sortować po stronie klienta (np. JavaScript). Tu z pomoca przychodzi nam biblioteka <a href="http://kryogenix.org/code/browser/sorttable/">sorttable</a> napisana właśnie w <em>JavaScript</em>. Skuteczna i prosta w użyciu. Spójrzcie na <a href="http://onjin.net/misc/sorttable/">mały przykład z opisem.</a>

I nie lepiej tak ?
