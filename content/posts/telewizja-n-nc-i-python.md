---
title: "Telewizja N (nc+) i python"
date: 2013-10-12T01:26:16
slug: telewizja-n-nc-i-python
tags: ["python","github","cli"]
cover: /img/cover-python1.jpg
---

Aby się przeklikać przez program na http://n.pl/ i jeszcze znaleźć interesujący program, to jest ponad moje siły.

Napisałem więc na szybko narzędzie działające w shellu, które pozwala przeglądać oraz przeszukiwać program ze strony
n.pl https://github.com/onjin/ntv/.

Instalacja
----------
Program napisany jest w **Pythonie** i dystrybuowany jako **egg**

{{< highlight bash >}}

    $ pip install ntv
    $ ntv-cli --help
{{< /highlight >}}


Kanały
------

Lista wszystkich kanałów nadających dzisiaj:

 * ntv-cli channels

Lista kanałów zawierających w nazie 'filmbox' (obojętne czy małe czy duże litery):

 * ntv-cli channels filmbox

Wyszukanie kanałów na wybrany dzień:

 * ntv-cli channels -d 2013-10-13
 * ntv-cli channels filmbox -d 2013-10-13

Programy
--------

Lista wszystkich programów nadawanych dzisiaj:

 * ntv-cli movies

Lista programów nadawanych na kanałach mający w nazie 'polsat':

 * ntv-cli movies polsat

Lista programów nadawanych na kanałach 'polsta' zawierająca w nazie słowo 'mecz':

 * ntv-cli movies polsat -t mecz

Wyszukanie programów na inny dzień:

 * ntv-cli movies polsat -t mecz -d 2013-10-13
