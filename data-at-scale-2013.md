# Data at Scale 2013

## Dropbox

- Consider looking at Dropbox APIs for an example of data delivery

- Dropbox is built on mysql from the start
    - they keep the snapshot of file blocks in mysql
    - they move their revision data to their secondary store

- Dropbox chose to ignore compression

- Look into XLDB 2013 / 2014

- look into MySQL 5.6 global transaction ids

- Dropbox Edgestore is roughly modeled on facebook Tao file system

- dropbox's workload is roughly 50 / 50 read / write -- more write heavy than typical

- txns across shards are not currenlty implemented; maybe in the future
    - their colo guid helps to locate similiar data, reducing the need for txns across shards

## Pinterest talk

### AWS

- they use the high 4xl instances

## Pinterest experimments wth Hbase talk

- Varun

# Cloudera

- apache caching project on hdfs

- flume interceptors

# Instagram talk

- postgres shop
- they are successfully using redis

# Facebook talk: Large scale low latency storage

- Harrison XX
- read the Tao paper

- each region has a full copy of their social graph

- 2BB reqeusts / second to Tao
- 45MM IOPS to mysql

## mcrouter

- Ryan McElroy

- FB sees about equal usage of memcache and tao; a surprising result
- read paper "scaling memcache at Facebook" 2013

- delete hold-offs during cold cache reload
- mcrouter is going to be open-sourced; the work is in progress
    - McElroy said mcrouter source won't compile outside of FB yet
    - written in C/C++

## Rocksdb talk

- Druba
- the goal here is the embedded DB space, aka like Berkeley DB

- LevelDB
    - a well written component, with good docs

- saw write amplification at ~60 - 100 GB DB size

- wormhole is the FB technology that answers the rocksdb replication strategy
- rocksdb has an API to access the txn log

## Jay Parikh talk

- open compute project
- top of rack switch

Wormhole contact. Liat@facebook.com

Karthikz twitter handle
Karthik@twitter.com


