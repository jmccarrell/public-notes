# Notes from _Hadoop with Python_ ebook

## HDFS

my home directory on HDFS is named `/user/jmccarre`

my home directory is assumed when the empty string is given

- ls HDFS

        jmccarre at dev-custom-explorer01 in ~
        $ hdfs dfs -ls /
        Found 14 items
        drwxr-xr-x   - akamai  supergroup          0 2014-08-18 15:34 /Export
        drwxrwxrwx   - akamai  supergroup          0 2014-12-01 01:30 /SummaryFeeds
        drwxrwxrwx   - akamai  supergroup          0 2014-10-21 13:50 /Trash
        drwxr-xr-x   - akamai  supergroup          0 2014-08-18 15:38 /_distcp_logs_vbj920
          ...

- mkdir / rmdir

        $ hdfs dfs -mkdir /user

        jmccarre at dev-custom-explorer01 in ~
        $ hdfs dfs -mkdir foobar
        jmccarre at dev-custom-explorer01 in ~
        $ hdfs dfs -ls -R
        drwxr-xr-x   - jmccarre supergroup          0 2015-11-05 14:45 .sparkStaging
        drwxr-xr-x   - jmccarre supergroup          0 2015-11-17 19:08 foobar
        jmccarre at dev-custom-explorer01 in ~
        $ hdfs dfs -rmdir foobar
        jmccarre at dev-custom-explorer01 in ~
        $ hdfs dfs -ls -R
        drwxr-xr-x   - jmccarre supergroup          0 2015-11-05 14:45 .sparkStaging

- cp to HDFS
    - with `-put`

            $ hdfs dfs -put /home/hduser/input.txt /user/hduser

    - moves input.txt from the local file system to the HDFS home directory of user `hduser`

- cp from HDFS
    - with `get` or `cat`

            $ hdfs dfs -cat input.txt
              ...
            $ hdfs dfs -get input.txt /home/hduser

## Snakebite

Snakebit is a pure-python client that talks to HDFS via its RPC definition with protobufs.

The major difference between snakebite and hdfs dfs is that snakebite is a pure Python client and does not need to load any Java libraries to communicate with HDFS. This results in quicker interactions with HDFS from the command line.
