CREATE DATABASE IF NOT EXISTS default;  
USE default;  
  
CREATE TABLE IF NOT EXISTS weather  
(  
    id Int32,  
    temperature Int32,  
    wind_speed Float64  
) ENGINE = MergeTree() ORDER BY id;  
  
-- Creating the target table with AggregatingMergeTree engine  
CREATE TABLE IF NOT EXISTS weather_aggregation  
(  
    id Int32,  
    average_temperature Float64,  
    average_wind_speed Float64  
) ENGINE = AggregatingMergeTree() ORDER BY id;  
  
-- Creating a materialized view for aggregation  
CREATE MATERIALIZED VIEW IF NOT EXISTS weather_aggregated  
    TO weather_aggregation  
AS  
SELECT id,  
       avg(temperature) AS average_temperature,  
       avg(wind_speed)  AS average_wind_speed  
FROM weather  
GROUP BY id;