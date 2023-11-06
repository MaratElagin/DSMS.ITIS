1. run hadoop-hive cluster
`docker-compose -p hadoop-hive up -d`
2. Copy dataset to  hive-server container
`docker cp products.csv hive-server:opt/hive/products.csv`
3. Login to hive-server
 `docker exec -it hive-server bash`
 4. Create database and table
 ```
create database if not exists testdb;
use testdb;
CREATE TABLE products (
asin STRING,
title STRING,
imgUrl STRING,
productURL STRING,
stars STRING,
reviews STRING,
price STRING,
isBestSeller STRING,
boughtInLastMonth STRING,
categoryName STRING
)
ROW FORMAT SERDE 'org.apache.hadoop.hive.serde2.OpenCSVSerde'
WITH SERDEPROPERTIES (
'separatorChar' = ',',
'quoteChar' = '\"'
)
STORED AS TEXTFILE;
 ```
 5. Check table information
 `describe formatted products;`
 6. Fill table from csv file
 `load data local inpath '/opt/hive/products.csv' overwrite into table products;`
 7. SQL-query: Средняя цена по категории, у товаров, которые купили хотя бы 1 раз за последний месяц и звезд больше 4
 ```
SELECT categoryName, AVG(CAST(price AS DECIMAL)) AS avg_price
FROM products
WHERE CAST(boughtInLastMonth AS INTEGER) > 0 AND CAST(stars AS DECIMAL) > 4.0
GROUP BY categoryName;
 ```
