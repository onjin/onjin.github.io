---
title: "Fast sentry instance using docker"
date: 2013-09-18
tags: ["develop","docker","linux"]
language: en
links:
    - https://sentry.io/
    - https://www.docker.com/
    - url: /pl/blog/startujemy-sentry-przy-pomocy-dockera/
      title: Read in Polish
      section: Alternatives
---

![Cover](../../assets/images/cover-containers1.jpg)

How to quickly spin up private <a href="https://sentry.io">Sentry</a> instance using only docker.

<!-- more -->

## Requirements

You need docker and postgresql database

 * https://www.docker.com/


## Running

If you have docker installed and postgres database created you can:

``` bash

# pull sentry image
docker pull onjin/sentry

# install sentry database
docker run  \
    -e SENTRY_DBHOST=your.db.address \
    -e SENTRY_DBNAME=sentrydbname \
    -e SENTRY_DBUSER=dbuser \
    -e SENTRY_DBPASS=dbpass \
    -p :7365 onjin/sentry upgrade

# run sentry instance
docker run -d \
    -e SENTRY_DBHOST=your.db.address \
    -e SENTRY_DBNAME=sentrydbname \
    -e SENTRY_DBUSER=dbuser \
    -e SENTRY_DBPASS=dbpass \
    -p :7365 onjin/sentry start

```

and open browser at address:

 * host: http://localhost:7365/
