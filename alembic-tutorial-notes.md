## Alembic Tutorial work

### basic operations:

```
$ alembic current
INFO  [alembic.runtime.migration] Context impl MySQLImpl.
INFO  [alembic.runtime.migration] Will assume non-transactional DDL.
(alembic-tutorial) jeffmccarrell at pavo in /j/proj/alembic-tutorial
$ alembic heads
(alembic-tutorial) jeffmccarrell at pavo in /j/proj/alembic-tutorial
$ alembic history
```

### todo

- read about the alembic directives at [Operation Reference](http://alembic.zzzcomputing.com/en/latest/ops.html#ops)

### notes

- alembic stores the revision the DB is at in a table called: `alembic_version`

### first upgrade:

```
$ alembic upgrade head
INFO  [alembic.runtime.migration] Context impl MySQLImpl.
INFO  [alembic.runtime.migration] Will assume non-transactional DDL.
INFO  [alembic.runtime.migration] Running upgrade  -> ecca6a669e51, create account table.
```

- so now the version in the DB is as expected:

```
$ mysql --login-path=local test -e 'select version_num from alembic_version'
+--------------+
| version_num  |
+--------------+
| ecca6a669e51 |
+--------------+
```

----

- √ [start here](http://alembic.zzzcomputing.com/en/latest/tutorial.html#running-our-second-migration)

- √ continue on with [Auto Generating Migrations](http://alembic.zzzcomputing.com/en/latest/autogenerate.html)

### autogenerate

from the docs:

> Autogenerate will detect:
>> table additions, removals
>> column additions, removals
>> change of nullable status on columns
>> basic changes in indexes and explicitly named unique constraints
>> basic changes in foreign key constraints

> Autogenerate can optionally detect:
>> change of column type.
>> change of server default

- column type is triggered by configuring a `compare_type` parameter
- similiarly, configured via `compare_server_default`

> Autogenerate cannot detect
>> changes of table name.  these will be emitted as an add/drop pair, and should be hand-edited into a name change instead.
>> changes of column name.
>> anonymously named constraints.
>> Special sqlalchemy types, like Enum.

> Autogenerate cannot currently, but eventually will detect:
>> some free-standing constraint additions and removals, like CHECK, PRIMARY KEY
>> Sequence additions, and removals.

### alter column

> MySQL has special requirements here, since MySQL cannot ALTER a column without a full specification. When producing MySQL-compatible migration files, it is recommended that the existing_type, existing_server_default, and existing_nullable parameters be present, if not being altered.

**Mon Oct  3 14:41:15 PDT 2016**

## create my first migration


