1. run pulsar cluster: `docker-compose up -d`
2. Run producer: `python3 python/producer.py`
3. Run consumer: `python3 python/consumer.py`
4. Produce messages via command line.
5. Ensure that weather data inserted into postgres weather table.
6. Stop producer and consumer.
7. Login to broker: `docker exec -it broker bash`
8. Update schema compatibility to BACKWARD_TRANSITIVE:
`/pulsar/bin/pulsar-admin namespaces set-schema-compatibility-strategy --compatibility BACKWARD_TRANSITIVE public/default`
9. Comment `wind_speed` property in `weatherMessage` class.
10. Run producer and consumer. Send messages
11.  See postgres weather table.
12. Verify schema versions:
- First schema: `/pulsar/bin/pulsar-admin schemas get --version 0 persistent://public/default/weather`
- Second schema:`/pulsar/bin/pulsar-admin schemas get persistent://public/default/weather`


[**Screencast link**](https://drive.google.com/file/d/1y8lWEFJHNPLiKvcEnmr5Tmxz3d0ex_MD/view?usp=drive_link)
