1.  Create topic in pulsar.
```sh
/pulsar/bin/pulsar-admin topics create public/default/weather-topic
```
2. Create sink	pulsar with clickhouse
```sh
/pulsar/bin/pulsar-admin sinks create \
--tenant "public" \
--sink-type 'jdbc-clickhouse' \
--name 'orders-connector' \
--inputs "persistent://public/default/weather-topic" \
--parallelism 1 \
--sink-config-file /connector-config.yaml
```
 3. Connect to clickhouse DB and create weather table with mergeTree
Run sql script `databaseInit.sql`
4.  Run producer, send some data
5. Ensure that data inserts automatically to clickhouse