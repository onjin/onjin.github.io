---
title: "git, svn i puste katalogi"
date: 2009-01-12T20:47:59
tags: ["git","tools"]
---
<html><body><p>Importując repozytorium svn'a poprzez <strong>git-svn</strong> tracimy puste katalogi, co czasem nie jest przyjemne. W dodatku to przecież nasze katalogi i chcemy je mieć ;)</p>


<p>Dziś mnie trochę to przycisnęło więc, pogadałem chwilę z google i znalazłem użyteczny skrypt <a href="http://github.com/gma/git-me-up">git-me-up</a>.</p>



<p>Wystarczy pobrać sam plik <strong>git-me-up</strong>, nadać mu prawa wykonywania i wykonać:</p>

<blockquote>

git-me-up http://svn.somerepo.com/path/to/project ./project

</blockquote>

<p>a skrypt sam stworzy repozytorium git, zaimportuje wszystkoz repozytorium svn, utworzy brakujące puste katalogi i stworzy w razie potrzeby plik <strong>.gitignore</strong> na podstawie svn:ignore.</p>

<p>i już...</p></body></html>
