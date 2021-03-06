## acerno notes

- To count the rows across the many event_d tables, query over the information_schema:

```sql
SELECT table_name, table_rows
FROM information_schema.tables
WHERE table_schema = 'imi_archive'
AND table_name LIKE 'event_d_2010_06_%'
```

- To get information in csv format, use:

```sql
FIELDS TERMINATED BY ',' ENCLOSED BY '"'
LINES TERMINATED BY '\r\n';
```

- Another way to get this same effect is with -T and -t.  E.g:

        jeff-dev-> mysqldump -t -u root -pimi2ndpass mineware im_d_2010_06_15 -T /tmp

- From Andrew about mysql memory tables:

> Jeff…depending on how u wanna do this…either within MySQL or from a perl script (probably) you need to set the heap size for the memory u want available for ur test table:

`SET max_heap_table_size = 15 * 1024 *1024 *1024`

> should getcha to 16Gig.  u can change that to whatever.  I had it like that so I could visually see Kbytes, MB and GB iterations way back in the beginning J

> Stays this way until u drop the table or restart the mysql server.


`SHOW variables LIKE 'max_heap_table_size'`

will show u what u have.

table is what you think it is:

```sql
CREATE TABLE blah_blah
imi_id varchar(30) NOT NULL,
rev_count smallint UNSIGNED NOT NULL,
PRIMARY KEY(imi_id) ) ENGINE=MEMORY
```

you s/b all set. Give a shout if u want/need anything else.

----

On acerno RHEL 5 boxes, I install the version of the mysql server, via an RPM package, which is distributed in /usr/local/src/installed

```
[root@ddev-ad ~]# rpm -Uvh /usr/local/src/installed/MySQL-*
warning: /usr/local/src/installed/MySQL-client-standard-5.0.27-0.rhel4.x86_64.rpm: V3 DSA signature: NOKEY, key ID 5072e1f5
Preparing...                ########################################### [100%]
	package MySQL-shared-compat-5.0.27-0.rhel4 is already installed
	package MySQL-devel-standard-5.0.27-0.rhel4 is already installed
[root@ddev-ad ~]# rpm -Uvh /usr/local/src/installed/MySQL-server-standard-5.0.27-0.rhel4.x86_64.rpm warning: /usr/local/src/installed/MySQL-server-standard-5.0.27-0.rhel4.x86_64.rpm: V3 DSA signature: NOKEY, key ID 5072e1f5
Preparing...                ########################################### [100%]
   1:MySQL-server-standard  ########################################### [100%]
PLEASE REMEMBER TO SET A PASSWORD FOR THE MySQL root USER !
To do so, start the server, then issue the following commands:
/usr/bin/mysqladmin -u root password 'new-password'
/usr/bin/mysqladmin -u root -h ddev-ad password 'new-password'
See the manual for more instructions.

NOTE:  If you are upgrading from a MySQL <= 3.22.10 you should run
the /usr/bin/mysql_fix_privilege_tables. Otherwise you will not be
able to use the new GRANT command!

Please report any problems with the /usr/bin/mysqlbug script!

The latest information about MySQL is available on the web at
http://www.mysql.com
Support MySQL by buying support/licenses at http://shop.mysql.com
Starting MySQL SUCCESS!
```

----

- set up the usual dev mysql root password: it was the production root password.

```
/usr/bin/mysqladmin -u root -p password 'imi2ndpass'
/usr/bin/mysqladmin -u root -p -h ddev-ad password 'imi2ndpass'
```

----

- set up the imiuser account.

- Find existing permissions:

```
mysql> select User, Host from user where User = 'imiuser';
+---------+-----------+
| User    | Host      |
+---------+-----------+
| imiuser | localhost |
+---------+-----------+
1 row in set (0.00 sec)
```

Drop existing and add the dev standard recipe.

```
DROP USER imiuser@'%';
CREATE USER imiuser@'%' IDENTIFIED BY PASSWORD '*BDC25F6727D9A859A700AC7D5426A398B136099F';
GRANT SELECT, INSERT, UPDATE, DELETE, LOCK TABLES ON `imi_web`.* TO imiuser@'%';
GRANT SELECT, INSERT, UPDATE, DELETE, LOCK TABLES ON `vt_web`.* TO imiuser@'%';
GRANT SELECT, INSERT, UPDATE, DELETE, LOCK TABLES ON `ad_web`.* TO imiuser@'%';
GRANT SELECT, INSERT, UPDATE, DELETE, LOCK TABLES ON `imi`.* TO imiuser@'%';
GRANT RELOAD ON *.* TO imiuser@'%';
```

then check:

`show grants for imiuser@'%'\G`

```
mysql> show grants for imiuser@'%'\G
*************************** 1. row ***************************
Grants for imiuser@%: GRANT RELOAD ON *.* TO 'imiuser'@'%' IDENTIFIED BY PASSWORD '*BDC25F6727D9A859A700AC7D5426A398B136099F'
*************************** 2. row ***************************
Grants for imiuser@%: GRANT SELECT, INSERT, UPDATE, DELETE, LOCK TABLES ON `imi`.* TO 'imiuser'@'%'
*************************** 3. row ***************************
Grants for imiuser@%: GRANT SELECT, INSERT, UPDATE, DELETE, LOCK TABLES ON `imi_web`.* TO 'imiuser'@'%'
*************************** 4. row ***************************
Grants for imiuser@%: GRANT SELECT, INSERT, UPDATE, DELETE, LOCK TABLES ON `vt_web`.* TO 'imiuser'@'%'
*************************** 5. row ***************************
Grants for imiuser@%: GRANT SELECT, INSERT, UPDATE, DELETE, LOCK TABLES ON `ad_web`.* TO 'imiuser'@'%'
5 rows in set (0.00 sec)
```

- and remotely connect:

```
jeff-dev-> mysql -h ddev-ad ad_web
Welcome to the MySQL monitor.  Commands end with ; or \g.
```

- works.

- I had to drop these other permissions, particularly the ''@localhost entry to get things to work as I wanted them to.

```
mysql> select User, Host, Password from user;
+---------+---------------+-------------------------------------------+
| User    | Host          | Password                                  |
+---------+---------------+-------------------------------------------+
| root    | localhost     | *83C3D0BE863E154EAB2D9B4411019241EE1FF044 |
| root    | danner-ad-dev |                                           |
|         | danner-ad-dev |                                           |
|         | localhost     |                                           |
| imiuser | %             | *BDC25F6727D9A859A700AC7D5426A398B136099F |
+---------+---------------+-------------------------------------------+
5 rows in set (0.00 sec)
```

----

- Set up new users on new DBs

- dbname: usg
- user1: admin level, can do structural changes to the DB      usgadmin
- user2: web access,  can write rows into the tables.          usg

- usg password: au2cash
- password('au2cash'): *B13086066537FAFCFF07D4FA07006C974BA12958

- usgadmin password: melt1064
- (Au's melting point is 1064.3 degrees C)
- password('melt1064'): *3111F7D08244C4C0D739F2099FF6A6A1B27A810E

```
CREATE DATABASE usg;

DROP USER usguser@'%';
CREATE USER usguser@'%' IDENTIFIED BY PASSWORD '*B13086066537FAFCFF07D4FA07006C974BA12958';
GRANT SELECT, INSERT, UPDATE, DELETE, LOCK TABLES ON `usg`.* TO usguser@'%';
GRANT RELOAD ON *.* TO usguser@'%';

DROP USER usgadmin@'%';
CREATE USER usgadmin@'%' IDENTIFIED BY PASSWORD '*3111F7D08244C4C0D739F2099FF6A6A1B27A810E';
GRANT ALL ON usg.* TO usgadmin@'%';
```

----

- An example of importing CSV data converting dates in `YYYY/MM/DD` format so they get read:

```
load data local infile 'issue_mo_dataset.csv'
into table issue_mo
fields terminated by ','
lines terminated by '\r\n'
ignore 1 lines
(issue_key, CAN_COV_PRC, ISS_CD, US_COV_PRC,
 @ON_SALE_DATE, @OFF_SALE_DATE)
 set  ON_SALE_DATE=str_to_date(@ON_SALE_DATE, '%m/%d/%Y'),
     OFF_SALE_DATE=str_to_date(@OFF_SALE_DATE, '%m/%d/%Y');
```

----

- provision a user with permissions
- an example of a mysql stored procedure

```sql
-- GCW Fulfillment system
--  provision the mysql user for the system
-- execute as e.g. (NB the statement delimiter)
--  mysql --delimiter=// -u root -p < create-user.sql

-- NB In recent mysql versions, dropping a user also drops all the permissions
--  for individual tables, so these drop routines effectively clear out all
--  permissions state for the ffill user.

use mysql//
-- drop a user given their name and host
--  useful if you know all of the combinations of user and hostname to drop a priori
drop procedure if exists drop_if_user_exists//
create procedure drop_if_user_exists(in username varchar(16), in hostname varchar(60))
begin
    declare user_exists int default 0;
    set @du_stmt = concat('drop user ', "'", username, "'@'", hostname, "'");
    select count(User) into @user_exists
      from mysql.user
     where User=username
       and Host=hostname;
    if @user_exists then
       prepare drop_user from @du_stmt;
       execute drop_user;
       deallocate prepare drop_user;
    end if;
end//

-- find and drop all rows in the User table matching the username
--  used to clear all permission state
drop procedure if exists drop_user_rows//
create procedure drop_user_rows(in username varchar(16))
begin
    declare u varchar(16) default 'u';
    declare h varchar(60) default 'h';
    declare user_cursor cursor for select User, Host from mysql.user where User=username;

    open user_cursor;
    begin
        -- when the cursor runs out of data, do nothing, simply fall out of the loop
        declare exit handler for not found begin end;
        loop
            fetch user_cursor into u, h;
            set @du_stmt = concat('drop user ', "'", u, "'@'", h, "'");
            prepare drop_user from @du_stmt;
            execute drop_user;
            deallocate prepare drop_user;
        end LOOP;
    end;
    close user_cursor;
end//

-- provision the fulfillment user
call drop_user_rows('ffill')//
create user 'ffill'@'localhost' identified by password '*8DC302A4DB827B20531F80B91CE5E11309E42532'//
grant select, insert, update, delete, lock tables on `ffill`.* to `ffill`@`localhost`//
```

----

### Dealing with autocommit on a per connection basis

- autocommit is enabled by default on a per connection basis.
- For txns to work, one must disable autocommit.

Circa the 5.5 mysql server line, the documentation has this to say about autocommit:

1. One can specify autocommit = 0 in the init_connect variable, which can be specified in an option file:

```
    [mysqld]
    init_connect='SET autocommit=0'
```

or from the command line.
In servers > 5.5.8, there is a global autocommit system variable, so one can set this for all connections.

2. autocommit is of type boolean and has scope GLOBAL | SESSION

3. If a connection is re-established to the server automatically by the C lib, the server
   state associated with that connection is lost, including autocommit mode.
   (section 4.5.1.6.3. Disabling mysql Auto-Reconnect)

There is also the discussion of completion_type

I can set autocommit to 0 for the transactions I explicitly want to manage directly,
and leave autocommit alone for all other DB writes.
This seems like a good idea to me.
This means grepping for all rollback/commit (all 2 of them I think) then ensuring
there is a 'SET autocommit = 0;' executed on the cursor before everything else happens.

To the contrary, it looks like the safer thing to do is to use START TRANSACTION.
I need to understand what support, if any, the C mysql client API offers for START TRANSACTION.

----

### an aggregation can be stored in a variable:

```
mysql> set @x = (select count(*) from ff_member);
mysql> select @x;
+------+
| @x   |
+------+
|  923 |
```

but note that the subquery parentheses are necessary (why?):

```
mysql> set @x = select count(*) from ff_member;
ERROR 1064 (42000): You have an error in your SQL syntax; check the manual that corresponds...
```

Does mysql support coalesce?

----

**Fri Jul  3 21:13:00 PDT 2015**

## mysql utf8mb4

- here is a very [nice write up](https://mathiasbynens.be/notes/mysql-utf8mb4) by Mathias Bynens on utf8mb4, and why to prefer it in all
  cases over utf8.

- the preferred contents of /usr/local/etc/my.cnf shown there

```
    [client]
    default-character-set = utf8mb4

    [mysql]
    default-character-set = utf8mb4

    [mysqld]
    character-set-client-handshake = FALSE
    character-set-server = utf8mb4
    collation-server = utf8mb4_unicode_ci
```

- one can show this is working a couple of ways; client settings:

```
$ mysql --print-defaults
mysql would have been started with the following arguments:
--default-character-set=utf8mb4 --default-character-set=utf8mb4 --database=main
```

- and server settings (from Mathias above):

```
SHOW VARIABLES WHERE Variable_name LIKE 'character\_set\_%' OR Variable_name LIKE 'collation%';
```

----

**Thu Oct 27 19:23:54 PDT 2016**

## [mysql_config_editor](http://dev.mysql.com/doc/refman/5.7/en/mysql-config-editor.html)

- to set up my access on vega, I did:

```
$ mysql_config_editor set --login-path=local --host=localhost --user=root --password
Enter password:
```

**Sun Feb 12 11:38:13 PST 2017**

- when I downgraded to mariadb, I lost `--login-path` and `mysql_config_editor`.

**Wed Apr 19 12:42:21 PDT 2017**

- after I moved back to mysql, I restored `--login-path`.

**Thu Aug 31 08:19:19 PDT 2017**

## mysql copy table as CTAS

using LIKE will copy indices, but not foreign keys

```sql
create [temporary] table like 
```

with AS SELECT, you just get structure and data, no indices


- here is a reasonable article about the [use of temp tables as caches](http://www.databasejournal.com/features/mysql/article.php/3844811/Make-Your-MySQL-Queries-More-Efficient-with-Temporary-Tables.htm)

## Rick James mysql hints

this guy Rick James ([him on dba stackexchange](https://dba.stackexchange.com/users/1876/rick-james)) has put together a set of mysql notes that are quite helpful.

[MySQL docs by Rick James](http://mysql.rjweb.org/)

I found his [Ricks Rules of Thumb](http://mysql.rjweb.org/doc.php/ricksrots) particularly helpful

and there is a lot more there.
