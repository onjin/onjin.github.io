---
title: "Fast sentry instance using docker"
date: 2013-09-18T13:36:39
slug: blog20130918fast-sentry-instance-using-docker
tags: ["develop","docker","linux"]
img: /img/cover-containers1.jpg
toc: true
---


How to quickly spin up private <a href="https://sentry.io">Sentry</a> instance using only docker.

<!--more-->


Requirements
============

You need docker and postgresql database

 * https://www.docker.com/


Running
=======

If you have docker installed and postgres database created you can:

{{< highlight bash >}}

  # pull sentry image
  docker pull onjin/sentry

  # install sentry database
  docker run  -e SENTRY_DBHOST=your.db.address -e SENTRY_DBNAME=sentrydbname -e SENTRY_DBUSER=dbuser -e SENTRY_DBPASS=dbpass -p :7365 onjin/sentry upgrade

  # run sentry instance
  docker run -d -e SENTRY_DBHOST=your.db.address -e SENTRY_DBNAME=sentrydbname -e SENTRY_DBUSER=dbuser -e SENTRY_DBPASS=dbpass -p :7365 onjin/sentry start

{{< /highlight >}}

and open browser at address:

 * host: http://localhost:7365/
