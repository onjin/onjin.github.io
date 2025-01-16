---
title: "vim snippetsemu i liquibase"
date: 2010-08-11T18:45:35
url: /posts/blog20100811vim-snippetsemu-i-liquibase.html
tags: ["programowanie","tools","vim"]
links:
    - https://www.vim.org/
    - url: /pl/assets/files/xml_snippets.vim
      title: xml_snippets.vim
---

W [ostatnim wpisie](best-vim-plugins.md) pisałem o <a href="https://www.vim.org/scripts/script.php?script_id=1318">snippetsEmu</a> dla <a href="https://www.vim.org/">vim</a>'a,
a dziś załączam [xml_snippets.vim](/pl/assets/files/xml_snippets.vim), których używam przy pracy z <a href="https://www.liquibase.org/">liquibase</a>.</p>


**Liquibase** to całkiem miłe narzędzie napisane w Javie do śledzenia, zarządzania i wprowadzania zmian w bazach danych. Zmiany opisuje się w pliku (plikach) xml i wpisywanie oraz pamiętanie tej składni można sobie uprościć przy pomocy vim'a i snippetów.

Snippet umieszczamy razem z pozostałymi, najczęściej w <strong>.vim/after/ftplugin/</strong>.

Najprościej zacząć otwierając np. <em>migration.xml</em>, wpisując <em>lhelp</em> i wcisnąć <em>TAB</em>. Otrzymamy małą pomoc i możemy zaczynać wpisywać kolejną migrację :)</p>

* [xml_snippets.vim](/pl/assets/files/xml_snippets.vim)
