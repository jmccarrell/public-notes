----

install postgres, so I can try installing the psycopg2 driver.

```
$ brew install postgres
==> Downloading https://homebrew.bintray.com/bottles/postgresql-9.5.5.sierra.bottle.tar.gz
######################################################################## 100.0%
==> Pouring postgresql-9.5.5.sierra.bottle.tar.gz
==> Using the sandbox
==> /usr/local/Cellar/postgresql/9.5.5/bin/initdb /usr/local/var/postgres
==> Caveats
If builds of PostgreSQL 9 are failing and you have version 8.x installed,
you may need to remove the previous version first. See:
  https://github.com/Homebrew/homebrew/issues/2510

To migrate existing data from a previous major version (pre-9.0) of PostgreSQL, see:
  https://www.postgresql.org/docs/9.5/static/upgrading.html

To migrate existing data from a previous minor version (9.0-9.4) of PostgreSQL, see:
  https://www.postgresql.org/docs/9.5/static/pgupgrade.html

  You will need your previous PostgreSQL installation from brew to perform `pg_upgrade`.
  Do not run `brew cleanup postgresql` until you have performed the migration.

To have launchd start postgresql now and restart at login:
  brew services start postgresql
Or, if you don't want/need a background service you can just run:
  pg_ctl -D /usr/local/var/postgres start
==> Summary
🍺  /usr/local/Cellar/postgresql/9.5.5: 3,154 files, 35.1M
```

----

- pyscopg2 pip install:
- fails with:

    ld: library not found for -lssl

- and remembering my openssl notes:

```
$ brew info openssl
openssl: stable 1.0.2j (bottled) [keg-only]
SSL/TLS cryptography library
https://openssl.org/
/usr/local/Cellar/openssl/1.0.2j (1,695 files, 12M)
  Poured from bottle on 2016-09-29 at 08:18:49
From: https://github.com/Homebrew/homebrew-core/blob/master/Formula/openssl.rb
==> Dependencies
Build: makedepend ✘
==> Options
--universal
	Build a universal binary
--without-test
	Skip build-time tests (not recommended)
==> Caveats
A CA file has been bootstrapped using certificates from the SystemRoots
keychain. To add additional certificates (e.g. the certificates added in
the System keychain), place .pem files in
  /usr/local/etc/openssl/certs

and run
  /usr/local/opt/openssl/bin/c_rehash

This formula is keg-only, which means it was not symlinked into /usr/local.

Apple has deprecated use of OpenSSL in favor of its own TLS and crypto libraries

Generally there are no consequences of this for you. If you build your
own software and it requires this formula, you'll need to add to your
build variables:

    LDFLAGS:  -L/usr/local/opt/openssl/lib
    CPPFLAGS: -I/usr/local/opt/openssl/include
    PKG_CONFIG_PATH: /usr/local/opt/openssl/lib/pkgconfig
```

- so try:

```
$ LDFLAGS=-L/usr/local/opt/openssl/lib pip install psycopg2
Collecting psycopg2
  Using cached psycopg2-2.6.2.tar.gz
Building wheels for collected packages: psycopg2
  Running setup.py bdist_wheel for psycopg2 ... done
  Stored in directory: /Users/jeff/Library/Caches/pip/wheels/49/47/2a/5c3f874990ce267228c2dfe7a0589f3b0651aa590e329ad382
Successfully built psycopg2
Installing collected packages: psycopg2
Successfully installed psycopg2-2.6.2
```

- then running tox on one of the postgres variants worked.

```
$ tox -e py35-pytest30-django1.9-postgres
  ...
========================== 119 passed, 2 skipped in 61.15 seconds ==========================  
```

- so it should be possible to add support for python 3 and the mysqlclient driver.

----

- try getting the python 2.7 mysql test running.
- install 
