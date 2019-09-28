---
title: "Startujemy sentry przy pomocy dockera"
date: 2013-09-18T13:36:39
slug: blog20130918fast-sentry-instance-using-docker-pl
tags: ["develop","docker","linux"]
img: /img/cover-containers1.jpg
toc: true
---


Jak szybko uruchomić prywatną instancję <a href="https://sentry.io">Sentry</a> używając dockera.

<!--more-->


Wymagania
=========

Zainstaluj dockera:

 * https://www.docker.com/


Startujemy
==========

Gdy masz zainstalowanego dockera oraz postgresa wtedy można startować:

{{< highlight bash >}}

  # pull sentry image
  docker pull onjin/sentry

  # instalujemy bazę sentry
  docker run  -e SENTRY_DBHOST=your.db.address -e SENTRY_DBNAME=sentrydbname -e SENTRY_DBUSER=dbuser -e SENTRY_DBPASS=dbpass -p :7365 onjin/sentry upgrade

  # startujemy instancję sentry
  docker run -d -e SENTRY_DBHOST=your.db.address -e SENTRY_DBNAME=sentrydbname -e SENTRY_DBUSER=dbuser -e SENTRY_DBPASS=dbpass -p :7365 onjin/sentry start

{{< /highlight >}}

i otwieramy w przeglądarce adres:

 * host: http://localhost:7365/
