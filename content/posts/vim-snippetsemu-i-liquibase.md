---
title: "vim snippetsemu i liquibase"
date: 2010-08-11T18:45:35
slug: blog20100811vim-snippetsemu-i-liquibase
url: /posts/blog20100811vim-snippetsemu-i-liquibase.html
tags: ["programowanie","tools","vim"]
cover: /img/cover-code-editor.jpg
aliases:
    - /posts/blog20100811vim-snippetsemu-i-liquibase/index.html
---
W <a href="{{< ref "best-vim-plugins" >}}">ostatnim wpisie</a> pisałem o <a href="http://www.vim.org/scripts/script.php?script_id=1318">snippetsEmu</a> dla <a href="http://www.vim.org/">vim</a>'a, a dziś załączam <a href="/files/xml_snippets.vim">zestaw snippetów</a>, których używam przy pracy z <a href="http://www.liquibase.org/">liquibase</a>.</p>


**Liquibase** to całkiem miłe narzędzie napisane w Javie do śledzenia, zarządzania i wprowadzania zmian w bazach danych. Zmiany opisuje się w pliku (plikach) xml i wpisywanie oraz pamiętanie tej składni można sobie uprościć przy pomocy vim'a i snippetów.

Snippet umieszczamy razem z pozostałymi, najczęściej w <strong>.vim/after/ftplugin/</strong>.

Najprościej zacząć otwierając np. <em>migration.xml</em>, wpisując <em>lhelp</em> i wcisnąć <em>TAB</em>. Otrzymamy małą pomoc i możemy zaczynać wpisywać kolejną migrację :)</p>

* <a href="/files/xml_snippets.vim">xml_snippets.vim</a>
