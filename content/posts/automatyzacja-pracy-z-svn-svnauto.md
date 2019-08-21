---
title: "automatyzacja pracy z svn - svnauto"
date: 2007-01-07T00:00:57
slug: blog20070107automatyzacja-pracy-z-svn-svnauto
tags: ["tools", "svn", "svnauto"]
---
<body><a href="http://pmade.com/open-source-software/sc/">Svnauto</a> jest wrapperem konsolowej komendy 'svn', który automatyzuje i standaryzuje wykonywanie rozgałęzień (branches) i złączeń (merge).


SC jest skryptem napisanym w języku <a href="http://www.ruby-lang.org/">Ruby</a> i jest dostępny poprzez <a href="http://rubyforge.org/projects/rubygems/">RubyGems</a>:

    gem install svnauto --include-dependencies


Hmm, ale czemu to nie działa?
-----------------------------

Skrypt <strong>sc</strong> bazuje na komunikatach zwracanych przez komendę <strong>svn</strong> w języku angielskim, więc nie będzie działać poprawnie w innych lokalizacjach. Można to rozwiązać np. tak:


    mv /usr/bin/sc /usr/bin/sc.orig


stworzyć nowy plik /usr/bin/sc:

{{< highlight bash >}}

#!/bin/bash

LC_ALL=C

/usr/bin/sc.orig $*

{{< /highlight >}}

i nadać mu prawa do wykonywania (w przypadku systemów Linux):

    chmod 755 /usr/bin/sc

Podstawy na początek
--------------------

Standardowa praca z SC wygląda mniej więcej tak:

Konfigurujemy dostęp do naszego repozytorium (SC obsługuje ich wiele)

    sc config --add

Tworzymy nowy projekt (zostaniemy zapytani o repozytorium, którego chcemy użyc)

    sc create my-new-project

W naszym repozytorium zostanie dodany katalog my-new-project wraz ze strukturą:

{{< highlight bash >}}
  myproject:
    |
    +--trunk
    |   |
    |   +--project-files
    |
    +--branches
    |   |
    |   +--rel
    |   +--bug
    |   +--exp
    |
    +--tags
        |
        +--rel
        +--bug
        +--exp


{{< /highlight >}}


Do katalogu ze zródłami lokalnymi (domyślnie **~/src**, ale możemy to zmienić podczas konfigurowania repozytorium w SC) zostanie wyciągnięty
**trunk** naszego nowego projektu do katalogu **~/src/nazwa_repozytorium/my-new-project-trunk**.

W przypadku kolejnych pobrań projektu (np, na inną maszynę, dla innego użytkownika) wywołujemy komendę:

    sc checkout my-new-project

i dostaniemy domyślnie źródła trunk'a do lokalnej kopii. Używając opcji w linii komend (-r, -b, -e) możemy pobrać odpowiednio wybrany release, bug lub eksperymentalną gałąź.

Tu sobie pracujemy normalnie jak to z SVN'em bywa, add, commit, update.

Kolejne wydania
---------------

Aby wydać kolejną wersję naszego projektu wydajemy komendę:

    sc release 1.0.0

Nasz trunk zostanie skopiowany do <strong>branches/rel/1.0</strong> i <strong>tags/rel/1.0</strong> oraz do <strong>~src/nazwarepozytorium/my-new-project-rel-1.0</strong> zostanie wyciągnięty ten release.

Praca z błędami
---------------

Jeżeli znajdziemy błąd, wydajemy komendę:

    sc bug 1

gdzie <strong>1</strong> to numer błędu (przydzielony np przez <a href="http://trac.edgewall.org/">trac</a>'a). W naszym repozytorium zostanie założony katalog <strong>branches/bug/1</strong> i oczywiście trafi do nas jego lokalna kopia <strong>~/src/nazwarepozytorium/my-new-project-bug-1</strong>.

Po naprawieniu błędu zamykamy go (i zatwierdzeniu zmian przez 'commit' oczywiście):

    sc bug --close 1

Zostaniemy zapytani czy zrobić merge naszej poprawki do release 1.0, a następnie czy chcemy też tą poprawkę zmergować do trunk'u, gdzie najczęściej na wszystko się potulnie zgadzamy.

Wersje eksperymentalne
----------------------

Tworząc nowy eksperymentane rozgałęzienie kodu wydajemy komendę:

    sc exp new_feature

Podczas pracy z taką gałęzią przyda nam się możliwość złączenia zmian z <strong>trunk'a</strong> do nas:

    sc expt --up new_feature

oraz na zakończenie prac (lub w miarę potrzeb) złączenie gałęzi eksperymentalnej z trunkiem:

    sc exp --down new_feature

Co ja z tego mam
----------------

Dzięki <strong>svnauto</strong> możemy zapomnieć o podawaniu pełnej ścieżki do repozytorium (jest skonfigurowana na początku pracu), więc przeglądanie projektu umożliwia nam prosta komenda

    sc list my-new-project

Dodatkowo mamy porządek w naszym repozytorium. Nawet jeżeli będziemy potrzebowali złączyć kilka rozgałęzień w jeden niestandardowy projekt z różnymi poprawkami, łatwo nam jest odnaleźć wszystkie potrzebne nam gałęzie i pojedynczo połączyć.

Praca nad poprawkami i nowymi wersjami jest prosta dzięki automatycznemu łączeniu odpowiednich gałęzi. Oczywiście nie uwolni nas to od rozwiązywania konfliktów, ale operacje, które wykonujemy już prawie automatycznie (prawie robi różnicę, np literówki, błąd w nazwie gałęzi) są robione naprawdę automatycznie.

Dzięki temu możemy się skupić na pracy nad projektem, zamiast nad prowadzeniem repozytorium do projektu.
