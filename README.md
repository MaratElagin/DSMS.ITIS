1. run hadoop cluster
`docker-compose -p hadoop up`
2. Login to datanode1-1
`docker exec -it hadoop-datanode1-1 bash`
3. Send input data from container to hdfs
 `hdfs dfs -put inputdata/news.csv /news.csv`
 4. Run hadoop jar mapreduce
 ` hadoop jar hadoop-streaming-3.3.6.jar \  
 -files python/mapper.py,python/reducer.py -mapper python/mapper.py \
 -reducer python/reducer.py \
 -input /news.csv \
 -output /news_map_reduce_results`