.. title: Fast sentry instance using docker
.. slug blog20130918fast-sentry-instance-using-docker
.. date: 2013-09-18 13:36:39
.. tags: develop,docker,linux

You need docker and postgresql database

 * docker.io_

.. _docker.io: http://docker.io/


If you have docker installed and postgres database created you can:

.. code:: bash

    # pull sentry image
    docker pull onjin/sentry

    # install sentry database
    docker run  -e SENTRY_DBHOST=your.db.address -e SENTRY_DBNAME=sentrydbname -e SENTRY_DBUSER=dbuser -e SENTRY_DBPASS=dbpass -p :7365 onjin/sentry upgrade

    # run sentry instance
    docker run -d -e SENTRY_DBHOST=your.db.address -e SENTRY_DBNAME=sentrydbname -e SENTRY_DBUSER=dbuser -e SENTRY_DBPASS=dbpass -p :7365 onjin/sentry start


and open browser at address:

 * localhost_

.. _localhost: http://localhost:7365/
