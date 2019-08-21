---
title: "best vim plugins"
date: 2010-07-29T20:34:19
slug: blog20100729best-vim-plugins
url: /posts/blog20100729best-vim-plugins.html
tags: ["programowanie","python","tools","vim"]
cover: /img/cover-code-editor.jpg
---
Dziś robiłem porządki w ~/.vim/ . Aktualizacje do nowych wersji pluginów, wyrzucanie nieużywanych, porządki w ~/.vimrc. W trakcie tej pracy powstała lista pluginów, dzięki którym miło mi się pracuje

vimball
-------

Plugin zajmujący się pluginami dostarczanymi w paczkach .vba i pozwalający też takie paczki tworzyć, w praktyce potrzeby mi by instalować paczki .vba

 * http://www.vim.org/scripts/script.php?script_id=1502


snippetsEmu
-----------

Emuluje zachowanie snippetów z TextMate. Na przykład w pliku sometest.py wpisujesz 'for&lt;tab&gt;', uzupełniasz brakujące miejsca poruszając się klawiszem &lt;tab&gt; i otrzymujesz pełną pętle. Inne użyteczne snippety dla pythona to:

* <strong>prop</strong> - property
* <strong>get</strong> - def get_..
* <strong>set</strong> - def set_..
* <strong>def</strong> - def ..
* <strong>cm</strong> - classmethod
* <strong>cl</strong> - class
* <strong>ifn, ifmain, sb, sbu, sbl1, trye, tryf, tryef, unittest</strong>

Domyślnie dostarczone są 32 zestawy snippetów dla wielu języków programowania, opisu oraz frameworków (django, rails, symfony)

* http://www.vim.org/scripts/script.php?script_id=1318


neocomplcache
-------------

System tzw 'dopełniania' (podpowiadania) i to właśnie robi. Dopełnia nazwy metod, funkcji, atrybuty html, nazwy plików, itp. Trzeba po prostu zobaczyć i używać.

* http://www.vim.org/scripts/script.php?script_id=2620


project
-------

Bardzo prosty i skuteczny system pozwalający w bocznym oknie przeglądać wybrane lub wszystkie pliki z jednego lub wielu projektów. Każdy projekt ma zdefiniowany katalog, dzięki czemu otwarcie pliku z projektu (wciskamy 'enter' bedąc 'nad' plikiem) nastąpi równocześnie z przejściem do katalogu projektu. W ten sposób pliki projektu jak np 'tags' (ctags) zostaną poprawnie wczytane.

* http://www.vim.org/scripts/script.php?script_id=69


simple pairs
------------

Proste dopełnianie dla ", ', {, (, [ . Wpisanie znaku otwierającego powoduje automatyczne dopisanie znaku zamykającego. W przypadku {, (, [ gdy sami wpiszemy znak zamykający, nie zostanie on zdublowany. Kursor po prostu przesunie się dalej. Dla ", ' zostanie jednak stworzona kolejna para. Krótkie i skuteczne.

* http://www.vim.org/scripts/script.php?script_id=2339


vcscommand
----------

Plugin pozwalający wykonywać komendy dla CVS, SVN, SVK, git, bzr, and hg przy pomocy vim'a. Jeden zestaw komend bez względy na system kontroli wersji.

* http://www.vim.org/scripts/script.php?script_id=90


Niewiele tego, ale te pluginy, git (post/pre hooki), bash + zestaw skryptów wystarcza mi do pracy :)</body></html>
