---
title: "netbeans 6.5 + php5 + symfony + xdebug"
date: 2008-08-24T14:17:12
tags: ["php","webdev", "netbeans"]
---
W <a href="http://www.netbeans.org/community/releases/65/" title="Netbeasn 6.5 features">Netbeans 6.5</a> pojawia się support dla <a title="PHP - główna strona" href="http://www.php.net/">php5</a>. W/g informacji na stronie netbeans oznacza to:

* PHP Editor (Code completion, syntactic and semantic code highlighting)</li>
* Support for heredoc notation and PHTML</li>
* Debugging using Xdebug</li>
* Generators for MySQL database code snippets</li>

Temat, który najbardziej mnie interesował to jak zadziała debugging przy pomocy Xdebug. Postanowiłem sprawdzić to z istniejącym projektem bazującym na frameworku <a href="http://www.symfony-project.com/" title="php5 framework">Symfony</a>.</p>

1. Zainstalowałem netbeans pobierając odpowiednią paczkę ze strony <a title="Netbeans 6.5 beta download" href="http://download.netbeans.org/netbeans/6.5/beta/">netbeans</a>
2. Zainstalowałem Xdebug poprzez <strong>pecl install xdebug</strong> i dodaniu do konfiguracji <em>php</em> wierszy:

```bash
    # xdebug, jako zend_extension. ścieżke zmienić należy oczywiście na odpowiednią dla Twojej instalacji
    zend_extension=/usr/lib/php5/20060613+lfs/xdebug.so
    xdebug.remote_enable=on
```


3. dodałem w netbeans nowy projekt php z istniejącymi źródłami (projekt już mam uruchomiony), podając podaczas konfiguracji:

 * ścieżkę do źródeł projektu
 * adres url do projektu
 * katalog zawierający dane web (dostępne poprzez podany url projektu) w tym przypadku podkatalog 'web' w katalogu  projektu
 * punkt startowy czyli domyślny kontroler dla projektu, w tym przypadku 'frontend.php' w podkatalogu 'web'

4. następnie wystarczyło otworzyć plik projektu (np podany wyżej kontroler) z toolbar'a wybrać 'debug project' lub wciśnąć <strong>ctrl+F5</strong>

W tym momencie w uruchomionej przeglądarce (u mnie <a href="http://www.firefox.pl/">firefox 3.x</a> netbeans otwarł główny kontroler projektu wraz z parameterm XDEBUG_SESSION_START=netbeans-xdebug. W tym samym momencie w edytorze netbeans podświetlony został pierwszy wiersz kontrolera ... i już.

Możemy teraz ustawiać watche, breakpointy, poruszać się step out, step in, step up wybierając opcje z menu 'debug' lub używająć skrótów klawiszowych.

Dzięki krótkiemu testowi widać, że podstawowy debug działa i można sobie poużywać. Oczywiście jeżeli lubimy php5 i lubimy netbeans lub któreś z nich musimy używać ;)
